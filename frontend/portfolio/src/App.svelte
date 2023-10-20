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
  import Album from './routes/Album.svelte';


  let routes={
  "/":Home,
  "/gallery":Gallery,
  "/video":Video,
  "/about":About,
  "/contact":Contact,
  "/album":Album,


}


</script>

    



  <Nav
  item0="Home"
  item1="Photos"
  item2="Video"
  item3="Contact"
  item4="About"
  ></Nav>


<Router {routes}></Router>


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
