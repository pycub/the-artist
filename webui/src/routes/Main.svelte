<script>
    import { router } from "$lib/Router";
    let username = "";
    let password = "";
    let error = "";

    async function handleLogin() {
        try {
            const response = await fetch("http://localhost:8000/token", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: new URLSearchParams({
                    username,
                    password,
                    grant_type: "password",
                }),
            });

            if (!response.ok) throw new Error("Invalid credentials");

            const data = await response.json();
            localStorage.setItem("token", data.access_token);
            window.location.href = "/dashboard";
        } catch (e) {
            error = e.message;
        }
    }

    async function handleSignup() {
        try {
            const response = await fetch("http://localhost:8000/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: new URLSearchParams({
                    username,
                    password,
                    grant_type: "password",
                }),
            });

            if (!response.ok) throw new Error("Username already taken");

            const data = await response.json();
            localStorage.setItem("token", data.access_token);
            window.location.href = "/dashboard";
        } catch (e) {
            error = e.message;
        }
    }

    async function handleForgotPassword() {}
</script>

<img src="3.jpg" id="ux" usemap="#ux3" alt="ux3" />
<map name="ux3">
    <area
        shape="rect"
        coords="160,160,285,200"
        href="https://example1.com"
        alt="Login"
        on:click={() => handleLogin()}
    />
    <area
        shape="rect"
        coords="160,213,285,255"
        href="https://example2.com"
        alt="Signup"
        on:click={() => handleSignup()}
    />
    <area
        shape="rect"
        coords="160,263,285,280"
        href="https://example2.com"
        alt="ForgotPassword"
        on:click={() => handleForgotPassword()}
    />
</map>

<style>
    .input-group {
        margin-bottom: 1rem;
    }

    label {
        display: block;
        margin-bottom: 0.5rem;
        color: #4a5568;
    }

    input {
        width: 100%;
        padding: 0.5rem;
        border: 1px solid #e2e8f0;
        border-radius: 4px;
    }

    button {
        width: 100%;
        padding: 0.75rem;
        background: #4299e1;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    button:hover {
        background: #3182ce;
    }

    .error {
        color: #e53e3e;
        margin-bottom: 1rem;
    }
</style>
