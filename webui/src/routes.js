import Login from "./routes/Login.svelte";
import Main from "./routes/Main.svelte";
import Signup from "./routes/Signup.svelte";
// import Dashboard from "./routes/Dashboard.svelte";
import NotFound from "./routes/NotFound.svelte";
// import Story from "./routes/Story.svelte";

export const routes = {
  "/": Main,
  "/login": Login,
  "/signup": Signup,
  // "/dashboard": Dashboard,
  // "/Story": Story,
  "*": NotFound,
};
