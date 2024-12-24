import Login from "./routes/Login.svelte";
import Main from "./routes/Main.svelte";
import Signup from "./routes/Signup.svelte";
import ForgetPassword from "./routes/ForgetPassword.svelte";
import Journey from "./routes/Journey.svelte";
// import Dashboard from "./routes/Dashboard.svelte";
import NotFound from "./routes/NotFound.svelte";

export const routes = {
  "/": Main,
  "/login": Login,
  "/signup": Signup,
  "/forgetpassword": ForgetPassword,
  // "/dashboard": Dashboard,
  "/journey": Journey,
  "*": NotFound,
};
