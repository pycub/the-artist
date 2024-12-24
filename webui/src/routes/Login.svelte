<script>
    import NavigationButtons from "../lib/components/NavigationButtons.svelte";
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

<NavigationButtons />
<img src="4.jpg" id="ux4" alt="ux4" />
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

    <button type="submit" class="">Login</button>
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

    .error {
        color: #e53e3e;
        margin-bottom: 1rem;
    }
</style>
