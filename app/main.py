from datetime import datetime, timedelta

import jwt
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy import Column, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Svelte dev server URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Database Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)


class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    target_amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))


# Database setup
engine = create_engine("sqlite:///./app.db")
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)


# Dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Auth functions
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"


def create_token(username: str) -> str:
    expiration = datetime.utcnow() + timedelta(days=365)
    return jwt.encode(
        {"sub": username, "exp": expiration}, SECRET_KEY, algorithm=ALGORITHM
    )


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=401)
        return user
    except:
        raise HTTPException(status_code=401)


# Routes
@app.post("/signup")
def signup(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    if db.query(User).filter(User.username == form_data.username).first():
        raise HTTPException(status_code=400, detail="Username taken")

    hashed_password = pwd_context.hash(form_data.password)
    user = User(username=form_data.username, password=hashed_password)
    db.add(user)
    db.commit()

    token = create_token(form_data.username)
    return {"access_token": token, "token_type": "bearer"}


@app.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user.username)
    return {"access_token": token, "token_type": "bearer"}


@app.post("/goals")
def create_goal(
    title: str,
    target_amount: float,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict:
    goal = Goal(title=title, target_amount=target_amount, user_id=user.id)
    db.add(goal)
    db.commit()
    return {"id": goal.id, "title": goal.title, "target_amount": goal.target_amount}


@app.get("/goals")
def get_goals(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    goals = db.query(Goal).filter(Goal.user_id == user.id).all()
    return [
        {"id": g.id, "title": g.title, "target_amount": g.target_amount} for g in goals
    ]


@app.post("/expenses")
def create_expense(
    amount: float,
    description: str,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    expense = Expense(amount=amount, description=description, user_id=user.id)
    db.add(expense)
    db.commit()
    return {
        "id": expense.id,
        "amount": expense.amount,
        "description": expense.description,
    }


@app.get("/expenses")
def get_expenses(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    expenses = db.query(Expense).filter(Expense.user_id == user.id).all()
    return [
        {"id": e.id, "amount": e.amount, "description": e.description} for e in expenses
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
