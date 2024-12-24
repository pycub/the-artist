<script>
    import NavigationButtons from "../lib/components/NavigationButtons.svelte";
</script>

<NavigationButtons />
<img src="1.jpg" id="ux1" alt="ux1" />
<p>Not implemented yet, try to sign up with new creds</p>

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
        background: white;
        color: #696969;
    }

    button {
        width: 40%;
        padding: 0.75rem;
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
