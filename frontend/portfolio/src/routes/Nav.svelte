<script>
  export let item1, item2,item3
</script>




<header>
<nav class="navbar " role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="https://bulma.io">
        <img src="">
      </a>
  
      <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>
  
    <div id="navbarBasicExample" class="navbar-menu is-centered">
      <div class="navbar-start" style="flex-grow: 1; justify-content: center;"
      >
        <a class="navbar-item" href="#/">{item1}</a>
        <a class="navbar-item" href="#/video">{item2}</a>
        <a class="navbar-item" href="#/contact">{item3}</a>
      </div>
    </div>
  </nav>
</header>
<slot />


<style>
  nav{
    background-color: #e3f6f5;
  }
</style>