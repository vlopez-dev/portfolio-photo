<script>
  import Home from './routes/Home.svelte';
  import Nav from './routes/Nav.svelte';
  import Gallery from './routes/Gallery.svelte';
  import Footer from './routes/Footer.svelte';
  import Contact from './routes/Contact.svelte';
  import Video from './routes/Video.svelte';
  import Router from "svelte-spa-router"


  let routes={
  "/":Gallery,
  "/video":Video,
  "/contact":Contact,

}


</script>

    



  <Nav
  item1="Photos"
  item2="Video"
  item3="Contact"
  ></Nav>

<section id="Home" class=" home-section hero is-fullheight custom-component">
  <Home></Home>
</section>

<section id="photo" class="photo-gallery hero is-fullheight custom-component">
  <!-- <h1 class="title">Photos</h1> -->
  <Gallery> </Gallery>
</section>
<section id="video" class=" section-video hero is-fullheight custom-component">
  <!-- <h1 class="title" >Video</h1> -->
</section>
<section id="about" class=" about-section hero is-fullheight custom-component mt-6">
  <!-- <h1 class="title">About</h1> -->
</section>
<section id="contact" class=" contact-section hero is-fullheight custom-component">
  <!-- <h1 class="title">Contact</h1> -->
  <Contact></Contact>
</section>


<Footer></Footer>

<style>
 :global(body) {
    display: flex;
    color: white;
    flex-direction: column;
    place-items:normal;
    background-color: #fffffe;
	}

  .home-section {
    clip-path: polygon(0 0, 100% 0%, 100% 100%, 0 81%);
    background-color: #d1d1e9;
      }

  .section-video{
    clip-path: polygon(0 0, 100% 19%, 100% 100%, 0 100%);
    
    background-color: #d1d1e9;

  }

  .photo-gallery {
  }



  .about-section{

  }
  .contact-section{
    clip-path: polygon(0 0, 100% 19%, 100% 100%, 0 100%);

background-color: #bae8e8;
  }



  .background-img img{
    width: auto;
    height: auto;
  }
</style>
