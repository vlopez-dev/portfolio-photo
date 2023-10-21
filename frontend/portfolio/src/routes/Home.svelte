<script>
      import { scrollTo, scrollRef, scrollTop } from 'svelte-scrolling'
  import About from "./About.svelte";
  import Contact from "./Contact.svelte";
import Gallery from "./Gallery.svelte";
  import Video from "./Video.svelte";

 let showHome = true;
    let showNav = true;
    let showGallery = true;
    let showFooter = true;
    let showContact = true;
    let showVideo = true;
    let showAbout = true;

  function scrollToComponent(component) {
        const targetComponent = document.getElementById(component);
        if (targetComponent) {
            targetComponent.scrollIntoView({ behavior: 'smooth' });
        }
    }


</script>
<section  use:scrollRef={'home'} id="Home" class=" home-section hero is-large  custom-component" >
<div class="hero-body ">
    <div class="">
      <p class="title">
        Fullheight hero
      </p>
      <p class="subtitle">
        Fullheight subtitle
      </p>
    </div>
  </div>
</section>
<section use:scrollRef={'photo'} id="Photo" class="photo-gallery hero is-fullheight custom-component">
<Gallery></Gallery>
</section>
<section use:scrollRef={'video'} id="Video" class=" section-video hero is-fullheight custom-component">
<Video></Video>
</section>
<section use:scrollRef={'about'} id="About" class=" about-section hero is-fullheight custom-component mt-6">
<About></About>
</section>
<section use:scrollRef={'contact'} id="Contact" class=" contact-section hero is-fullheight custom-component">
<Contact></Contact>
</section>




<style>

.title{
    color: #272343;
    font-family: 'Montserrat', sans-serif;
    font-size: 8rem;
    text-align: center;
    /* line-height: 1.70rem; */
}


.subtitle{
    color: #272343;
    font-family: 'Montserrat', sans-serif;
    font-size: 3.6rem;
    text-align: center;
    /* line-height: 1.70rem; */

    }


    .home-section {
    /* clip-path: polygon(0 0, 100% 0%, 100% 100%, 0 81%); */
    background-color: #fffffe;
    background-image: url(https://images.unsplash.com/photo-1682687220742-aba13b6e50ba?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D);
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

</style>