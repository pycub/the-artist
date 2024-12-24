<script>
    import { router } from "../lib/Router";
</script>

<img src="4.jpg" style="width: 160px;" />
<!-- <img src="3.jpg" id="ux" usemap="#ux3" alt="ux3" /> -->
<!-- <map name="ux3"> -->
<!-- <area -->
<!-- shape="rect" -->
<!-- coords="130,132,230,163" -->
<!-- style="cursor: pointer;" -->
<!-- alt="Login" -->
<!-- on:click={() => router.navigate("/login")} -->
<!-- /> -->
<!-- <area -->
<!-- shape="rect" -->
<!-- coords="131,176,225,206" -->
<!-- alt="Signup" -->
<!-- style="cursor: pointer;" -->
<!-- on:click={() => router.navigate("/signup")} -->
<!-- /> -->
<!-- <area -->
<!-- shape="rect" -->
<!-- coords="129,214,226,226" -->
<!-- alt="ForgotPassword" -->
<!-- style="cursor: pointer;" -->
<!-- on:click={() => router.navigate("/forgetpassword")} -->
<!-- /> -->
<!-- </map> -->

<p>
    click <b
        on:click={() => router.navigate("/journey")}
        style="cursor: pointer;">here</b
    > to read the story
</p>

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
