<script>
    import { scrollTo, scrollRef, scrollTop } from 'svelte-scrolling'

  export let item0 ,item1, item2,item3,item4
  let currentSection = 'inicio'; // Sección inicialmente visible

  window.onload = function() {
  const burgerIcon = document.querySelector("#burger");
  const navMenu = document.querySelector("#nav-links");
  const navLinks = document.querySelectorAll(".navbar-item");

  burgerIcon.addEventListener("click", () => {
    navMenu.classList.toggle("is-active");
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      setTimeout(() => {
        navMenu.classList.remove("is-active");
      }, 500);
    });
  });
};


function handleScroll(event) {
    const scrollPosition = event.target.scrollTop;
    const sections = ['home','photo', 'video', 'about', 'contact']; // Las secciones de tu página

    // Calcula qué sección es visible en la ventana del navegador
    const visibleSection = sections.find(sectionId => {
      const sectionElement = document.getElementById(sectionId);
      if (sectionElement) {
        const sectionTop = sectionElement.offsetTop;
        const sectionBottom = sectionTop + sectionElement.offsetHeight;
        return scrollPosition >= sectionTop && scrollPosition < sectionBottom;
      }
      return false;
    });

    // Actualiza la sección actualmente visible
    currentSection = visibleSection || currentSection;

    
  }



</script>




<header class="pb-6">
<nav class="navbar is-fixed-top "  aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="https://bulma.io">
        <img src="" alt="">
        <h6>Nombre</h6>
      </a>
  
      <a id="burger" role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
  
    <div id="nav-links" class="navbar-menu is-centered">
      <div class="navbar-start" style="flex-grow: 1; justify-content: center;"
      >
      <a class="navbar-item btn "  use:scrollTo={{ref:'home', duration: 1500}} href="#Home">{item0}</a>

        <a class="navbar-item btn" use:scrollTo={{ref:'photo',duration:1000}} href="#Photo">{item1}</a>
        <a class="navbar-item btn" use:scrollTo={{ref:'video',duration:1000}} href="#Video">{item2}</a>
        <a class="navbar-item btn "use:scrollTo={{ref:'about',duration:1000}} href="#About">{item4}</a>

        <a class="navbar-item btn"  use:scrollTo={{ref:'contact',duration:1000}} href="#Contact">{item3}</a>

      </div>
    </div>
  </nav>
</header>
<slot />


<style>
  nav{
    background-color: #fffffe;
    
  }

.navbar-item{
  font-family: 'Montserrat', sans-serif;
}

  
</style>