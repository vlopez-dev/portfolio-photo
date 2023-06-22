<script>
  export let item1, item2,item3

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
</script>




<header class="pb-6">
<nav class="navbar is-fixed-top " role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="https://bulma.io">
        <img src="">
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
        <a class="navbar-item btn" href="#/">{item1}</a>
        <a class="navbar-item btn" href="#/video">{item2}</a>
        <a class="navbar-item btn" href="#/contact">{item3}</a>
      </div>
    </div>
  </nav>
</header>
<slot />


<style>
  nav{
    background-color: #fffffe;
  }




  
</style>