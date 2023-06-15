<script>
  import Home from './routes/Home.svelte';
  import Nav from './routes/Nav.svelte';
  import Gallery from './routes/Gallery.svelte';
  import Footer from './routes/Footer.svelte';
  import Contact from './routes/Contact.svelte';
  import Video from './routes/Video.svelte';
  import Router from "svelte-spa-router"


  let routes={
  "/":Home,
  "/video":Video,
  "/contact":Contact,

}


</script>

    



  <Nav
  item1="Home"
  item2="Video"
  item3="Contact"
  
  ></Nav>
  <Home></Home>

<Gallery></Gallery>
<Router {routes}></Router>

<Footer></Footer>

<style>
 :global(body) {
    display: flex;
    color: white;
    flex-direction: column;
    place-items:normal;
    background-color: #fef6e4;
	}
</style>
