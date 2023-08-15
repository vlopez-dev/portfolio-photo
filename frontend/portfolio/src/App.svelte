<script>
    import { scrollTo, scrollRef, scrollTop } from 'svelte-scrolling'

  import Home from './routes/Home.svelte';
  import Nav from './routes/Nav.svelte';
  import Gallery from './routes/Gallery.svelte';
  import Footer from './routes/Footer.svelte';
  import Contact from './routes/Contact.svelte';
  import Video from './routes/Video.svelte';
  import About from './routes/About.svelte';
  import Router from "svelte-spa-router"


  let routes={
  "/":Gallery,
  "/video":Video,
  "/contact":Contact,

}


</script>

    



  <Nav
  item0="Home"
  item1="Photos"
  item2="Video"
  item3="Contact"
  item4="About"
  ></Nav>

<section use:scrollRef={'home'} id="Home" class=" home-section hero is-large  custom-component">
  <Home></Home>
</section>

<section use:scrollRef={'photo'} id="Photo" class="photo-gallery hero is-fullheight custom-component">
  <Gallery> </Gallery>
</section>
<section use:scrollRef={'video'} id="Video" class=" section-video hero is-fullheight custom-component">
  <Video></Video>
</section>
<section use:scrollRef={'about'} id="About" class=" about-section hero is-fullheight custom-component mt-6" >
  <About></About>
</section>
<section use:scrollRef={'contact'} id="Contact" class=" contact-section hero is-fullheight custom-component">
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
    /* clip-path: polygon(0 0, 100% 0%, 100% 100%, 0 81%); */
    background-color: #fffffe;
    background-image: url(../../portfolio/img/jessica-favaro-ycZxjWxFBMk-unsplash.jpg);
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center center;
    height: 80%;
    
      }

      @media screen and (max-width: 768px) {
        .home-section {
        background-size: cover;
        background-position: center center;
    }
}

  .section-video{
    /* clip-path: polygon(0 0, 100% 19%, 100% 100%, 0 100%); */
    
    background-color: #fffffe;

  }

  .photo-gallery {
    background-color: #fffffe;
  }



  .about-section{
    /* clip-path: polygon(0 0, 100% 19%, 100% 100%, 0 100%); */

  }
  .contact-section{

background-color: #fffffe;
  }


</style>
