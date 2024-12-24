import { writable } from "svelte/store";
import { router } from "./Router";

export const user = writable(
  JSON.parse(localStorage.getItem("user") || "null"),
);
export const token = writable(localStorage.getItem("token") || null);

export const auth = {
  async login(username, password) {
    const response = await fetch("http://localhost:8000/token", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ username, password, grant_type: "password" }),
    });

    if (!response.ok) throw new Error("Invalid credentials");

    const data = await response.json();
    localStorage.setItem("token", data.access_token);
    localStorage.setItem("user", JSON.stringify({ username }));

    token.set(data.access_token);
    user.set({ username });
  },

  logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    token.set(null);
    user.set(null);
    router.navigate("/");
  },

  async checkAuth() {
    const currentToken = localStorage.getItem("token");
    if (!currentToken) return false;

    try {
      const response = await fetch("http://localhost:8000/goals", {
        headers: { Authorization: `Bearer ${currentToken}` },
      });
      return response.ok;
    } catch {
      return false;
    }
  },
};
