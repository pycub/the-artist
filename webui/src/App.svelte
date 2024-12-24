<script>
    import { onMount } from "svelte";
    import { routes } from "./routes";

    let currentPath = window.location.pathname;
    let component = routes[currentPath] || routes["*"];

    onMount(() => {
        const handleRoute = () => {
            currentPath = window.location.pathname;
            component = routes[currentPath] || routes["*"];
        };

        window.addEventListener("popstate", handleRoute);
        return () => window.removeEventListener("popstate", handleRoute);
    });
</script>

<main>
    <svelte:component this={component} />
</main>

<svelte:head>
    <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
    />
</svelte:head>
