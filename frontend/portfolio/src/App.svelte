<script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import Nav from './routes/Nav.svelte';
  import Gallery from './routes/Gallery.svelte';
</script>
<header>
  <Nav></Nav>
</header>
<Gallery></Gallery>

<style>
 :global(body) {
    display: flex;
    color: white;
    flex-direction: column;
    place-items:normal;
    background-color: white;
	}
</style>
