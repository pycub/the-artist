<script>
  import { onMount } from 'svelte';
  import Login from './Login.svelte';
  import Signup from './Signup.svelte';
  let showLogin = true;
</script>

<main class="container">
  <div class="auth-box">
    <div class="tabs">
      <button
        class:active={showLogin}
        on:click={() => showLogin = true}>Login</button>
      <button
        class:active={!showLogin}
        on:click={() => showLogin = false}>Signup</button>
    </div>

    {#if showLogin}
      <Login />
    {:else}
      <Signup />
    {/if}
  </div>
</main>

<style>
  .container {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #f5f5f5;
  }

  .auth-box {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    width: 100%;
    max-width: 400px;
  }

  .tabs {
    display: flex;
    margin-bottom: 2rem;
  }

  button {
    flex: 1;
    padding: 0.5rem;
    border: none;
    background: none;
    cursor: pointer;
  }

  .active {
    border-bottom: 2px solid #4299e1;
    color: #4299e1;
  }
</style>

// Login.svelte
<script>
  let username = '';
  let password = '';
  let error = '';

  async function handleLogin() {
    try {
      const response = await fetch('http://localhost:8000/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
          username,
          password,
          grant_type: 'password'
        })
      });

      if (!response.ok) throw new Error('Invalid credentials');

      const data = await response.json();
      localStorage.setItem('token', data.access_token);
      window.location.href = '/dashboard';
    } catch (e) {
      error = e.message;
    }
  }
</script>

<form on:submit|preventDefault={handleLogin}>
  <div class="input-group">
    <label for="username">Username</label>
    <input
      type="text"
      id="username"
      bind:value={username}
      required
    />
  </div>

  <div class="input-group">
    <label for="password">Password</label>
    <input
      type="password"
      id="password"
      bind:value={password}
      required
    />
  </div>

  {#if error}
    <p class="error">{error}</p>
  {/if}

  <button type="submit">Login</button>
</form>

// Signup.svelte
<script>
  let username = '';
  let password = '';
  let error = '';

  async function handleSignup() {
    try {
      const response = await fetch('http://localhost:8000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
          username,
          password,
          grant_type: 'password'
        })
      });

      if (!response.ok) throw new Error('Username already taken');

      const data = await response.json();
      localStorage.setItem('token', data.access_token);
      window.location.href = '/dashboard';
    } catch (e) {
      error = e.message;
    }
  }
</script>

<form on:submit|preventDefault={handleSignup}>
  <div class="input-group">
    <label for="username">Username</label>
    <input
      type="text"
      id="username"
      bind:value={username}
      required
    />
  </div>

  <div class="input-group">
    <label for="password">Password</label>
    <input
      type="password"
      id="password"
      bind:value={password}
      required
    />
  </div>

  {#if error}
    <p class="error">{error}</p>
  {/if}

  <button type="submit">Sign Up</button>
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
