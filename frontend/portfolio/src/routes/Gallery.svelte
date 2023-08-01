<script>
    import { onMount } from "svelte";
    function handleClick(e) {
		console.log(e.detail.src)
	}
</script>
<section class="section">
    <div class="container is-fluid">
      <!-- <h2 class="title title-section">Photo</h2> -->
      <div class="columns ">
          <div class="column">
            <div class="gallery-item " data-index="">
              <figure class="image ">
                <img src="https://images.unsplash.com/photo-1689776574086-50ff04ae5dec?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
            </div>
          </div>
          <div class="column">
            <div class="gallery-item " data-index="">
              <figure class="image ">
                <img src="../../img/rob-potter-hjIBz9JeS3I-unsplash.jpg" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
            </div>
          </div>
          <div class="column">
            <div class="gallery-item " data-index="">
              <figure class="image">
                <img src="../../img/neom-w-yuRFSkbVw-unsplash.jpg" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
            </div>
          </div>
          <div class="column">
            <div class="gallery-item " data-index="">
              <figure class="image">
                <img src="https://images.unsplash.com/photo-1689192092151-5d8984fdd21d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
              
            </div>
          </div>
          <div class="column">
            <div class="gallery-item " data-index="">
              <figure class="image ">
                <img src="../../img/christopher-campbell-rDEOVtE7vOs-unsplash.jpg" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
              
            </div>
          </div>

          <div class="column">
            <div class="gallery-item " data-index="">
              <figure class="image ">
                <img src="../../img/ahmed-LKSGP7Jqqbw-unsplash (1).jpg" alt="" />
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
              
            </div>
          </div>

          <div class="column">
            <div class="gallery-item " data-index="">
              <figure class="image ">
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

<!-- 

  <section class="section">
    <div class="container is-fluid">
        <div class="columns">
            <div class="column">
              <div class="gallery-item" data-index="">
                <figure>
                <img src="https://source.unsplash.com/800x1000/?nature,water" onclick="openModal();currentSlide(1)">
                <img src="https://source.unsplash.com/800x550/?nature,water" onclick="openModal();currentSlide(4)">
                
              </div>

            </div>
            <div class="column">
                <img src="https://source.unsplash.com/800x600/?nature,water" onclick="openModal();currentSlide(2)">
                <img src="https://source.unsplash.com/800x650/?nature,water" onclick="openModal();currentSlide(5)">
            </div>
            <div class="column">
                <img src="https://source.unsplash.com/800x900/?nature,water" onclick="openModal();currentSlide(3)">
                <img src="https://source.unsplash.com/800x700/?nature,water" onclick="openModal();currentSlide(6)">
            </div>
        </div>

</section>
 -->






















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
  }

  /* .gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  } */




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
    background-color: #ff5722;
    color: white;
    border: none;
    cursor: pointer;
  }
</style>