<script>
import {push, pop, replace} from 'svelte-spa-router'

    import { onMount } from "svelte";
    function handleClick(e) {
		console.log(e.detail.src)
	}
</script>
<section class="section ">
    <div class="container">
      <h2 class="title title-section">Photo</h2>
      <div class="columns is-multiline">
          <div class="column is-4">
            <div class="gallery-item " data-index="">
              <figure class="image is-square">
                <img src="https://images.unsplash.com/photo-1689776574086-50ff04ae5dec?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button on:click={() => push('/album')} >Ver detalles</button>
                </div>
              </figure>
            </div>
          </div>
          <div class="column is-4">
            <div class="gallery-item " data-index="">
              <figure class="image is-square">
                <img src="https://images.unsplash.com/photo-1545341425-ee53bbfd2653?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
            </div>
          </div>
          <div class="column is-4">
            <div class="gallery-item " data-index="">
              <figure class="image is-square">
                <img src="https://images.unsplash.com/photo-1689851709772-aa131deb6e2d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
            </div>
          </div>
          <div class="column is-4">
            <div class="gallery-item " data-index="">
              <figure class="image is-square">
                <img src="https://images.unsplash.com/photo-1689192092151-5d8984fdd21d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
              
            </div>
          </div>
          <div class="column is-4">
            <div class="gallery-item " data-index="">
              <figure class="image is-square">
                <img src="../../img/christopher-campbell-rDEOVtE7vOs-unsplash.jpg" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
              
            </div>
          </div>
      </div>
    </div>
  </section>

<style>




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