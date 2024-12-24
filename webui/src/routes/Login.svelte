<script>
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
</script>

<form on:submit|preventDefault={handleLogin}>
    <div class="input-group">
        <label for="username">Username</label>
        <input type="text" id="username" bind:value={username} required />
    </div>

    <div class="input-group">
        <label for="password">Password</label>
        <input type="password" id="password" bind:value={password} required />
    </div>

    {#if error}
        <p class="error">{error}</p>
    {/if}

    <button type="submit">Login</button>
</form>

<style>
    /* Shared styles for Login.svelte and Signup.svelte */
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
