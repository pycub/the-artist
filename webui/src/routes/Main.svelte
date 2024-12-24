<script>
    import { router } from "../lib/Router";
</script>

<img src="3.jpg" id="ux" usemap="#ux3" alt="ux3" />
<map name="ux3">
    <area
        shape="rect"
        coords="160,160,285,200"
        alt="Login"
        on:click={() => router.navigate("/login")}
    />
    <area
        shape="rect"
        coords="160,213,285,255"
        alt="Signup"
        on:click={() => router.navigate("/signup")}
    />
    <area
        shape="rect"
        coords="160,263,285,280"
        alt="ForgotPassword"
        on:click={() => router.navigate("/forgetpassword")}
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
