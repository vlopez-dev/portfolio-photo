<script>
import {push, pop, replace} from 'svelte-spa-router'
import albums from '../albums'

    import { onMount } from "svelte";
    function handleClick(e) {
		console.log(e.detail.src)
	}
</script>
<section class="section ">
    <div class="container">
      <h2 class="title title-section">Photo</h2>
      <div class="columns is-multiline">
        {#each albums as album,i}
          
          <div class="column is-4">
            <div class="gallery-item " data-index="">
              <figure class="image is-square">
                <img src="{album.cover}" alt="" />
                <div class="album-info">
                  <h3>{album.title}</h3>
                  <button on:click={() => push(`/album/${i}`)}>Ver detalles</button>
                </div>
              </figure>
            </div>
          </div>
          {/each}

         
          
          
      </div>
    </div>
  </section>

<style>

/* ../../img/christopher-campbell-rDEOVtE7vOs-unsplash.jpg */


.title{
font-family: 'Montserrat', sans-serif;
font-size: 2.6rem;
    }

.title-section{
  font-family: 'Montserrat', sans-serif;
  font-size: 2.6rem;
  text-align: center;

}


    .gallery-item {
    cursor: pointer;
    box-shadow: 0 30px 30px -30px rgba(27, 26, 26, 0.315);

  }

  .gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }




  .album-info {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    opacity: 0; /* Ocultar por defecto, solo se mostrará al hacer hover */
    pointer-events: none; /* Evitar que los elementos dentro de este div sean clickeables */
    transition: opacity 0.3s;
  }
  .gallery-item:hover .album-info {
    opacity: 1;
    pointer-events: auto;
  }



  .album-info button {
    padding: 10px 20px;
    background-color: #6246ea;
    color: #fffffe;
    border: none;
    cursor: pointer;
  }
</style>