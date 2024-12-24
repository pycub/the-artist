<script>
    import { onMount } from "svelte";
    import { routes } from "./routes";
    import { user, token } from "./lib/Auth";

    const urlParams = new URLSearchParams(window.location.search);
    const isOnHome = urlParams.ge;

    let currentPath = window.location.pathname;
    let component = routes[currentPath] || routes["*"];

    const protectedRoutes = ["/dashboard", "/goals", "/expenses"];

    async function handleRoute() {
        currentPath = window.location.pathname;

        if (protectedRoutes.includes(currentPath) && !$token) {
            window.location.pathname = "/";
            return;
        }

        component = routes[currentPath] || routes["*"];
    }

    onMount(() => {
        handleRoute();
        window.addEventListener("popstate", handleRoute);
        return () => window.removeEventListener("popstate", handleRoute);
    });
</script>

<main>
    <svelte:component this={component} />
</main>
