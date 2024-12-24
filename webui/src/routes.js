import Login from "./routes/Login.svelte";
import Main from "./routes/Main.svelte";
import Signup from "./routes/Signup.svelte";
import ForgetPassword from "./routes/ForgetPassword.svelte";
// import Dashboard from "./routes/Dashboard.svelte";
import NotFound from "./routes/NotFound.svelte";
// import Story from "./routes/Story.svelte";

export const routes = {
  "/": Main,
  "/login": Login,
  "/signup": Signup,
  "/forgetpassword": ForgetPassword,
  // "/dashboard": Dashboard,
  // "/Story": Story,
  "*": NotFound,
};
