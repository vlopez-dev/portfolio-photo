<script>
  
  import { onMount } from "svelte";
  import { scrollTo, scrollRef, scrollTop } from 'svelte-scrolling'
  import About from "./About.svelte";
  import Contact from "./Contact.svelte";
  import Gallery from "./Gallery.svelte";
  import Video from "./Video.svelte";


  let home=[];



  onMount(async () => {
    try{
      const[homeResponse] = await Promise.all([
        fetch("http://127.0.0.1:8000/home/").then((response) => response.json()),
      ]);
      home = homeResponse;
      console.log(home)
    }catch(error){
      console.log(error);
    }
  });



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


<section  use:scrollRef={'home'} id="Home" >
  {#each home as home}
  <div class="hero is-medium is-primary has-background ">
    <img alt="Fill Murray" class="hero-background is-transparent parallax-image" src="{home.cover}" />
    <div class="hero-body">
      <div class="container">
        <h1 class="title">
          {home.title}
        </h1>
        <h3 class="subtitle">
          {home.subtitle}
        </h3>
      </div>
    </div>
  </div>
  {/each}
  </section>


<section use:scrollRef={'photo'} id="Photo" class="photo-gallery hero is-fullheight custom-component">
<Gallery></Gallery>
</section>
<section use:scrollRef={'video'} id="Video" class=" section-video hero is-fullheight custom-component">
<Video></Video>
</section>
<section use:scrollRef={'about'} id="About" class=" about-section hero is-fullheight custom-component">
<About></About>
</section>
<section use:scrollRef={'contact'} id="Contact" class=" contact-section hero is-fullheight custom-component">
<Contact></Contact>
</section>




<style>






.hero.has-background {
  position: relative;
  overflow: hidden;
}
.hero-background {
  position: absolute;
  object-fit: cover;
  object-position: center center;
  width: 100%;
  height: 100%;
}

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


    .home-section  {
   
    background-color: #fffffe; 
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