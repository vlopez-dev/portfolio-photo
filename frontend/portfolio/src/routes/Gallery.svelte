<script>
    import { onMount } from "svelte";
    function handleClick(e) {
		console.log(e.detail.src)
	}
</script>
<!-- <section class="section">
    <div class="container is-fluid">
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
  </section> -->



  <section class="section">
    <div class="container is-fluid">
        <div class="columns">
            <div class="column">
              <div class="gallery-item" data-index="">
                <figure>
                <img src="https://source.unsplash.com/800x1000/?nature,water" onclick="openModal();currentSlide(1)">
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
              </div>

            </div>
            <div class="column">
              <div class="gallery-item" data-index="">
                <figure>
                <img src="https://source.unsplash.com/800x600/?nature,water" onclick="openModal();currentSlide(2)">
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
            </div>
          </div>

            <div class="column">
              <div class="gallery-item">
                <figure>
                <img src="https://source.unsplash.com/800x900/?nature,water" onclick="openModal();currentSlide(3)">
                <div class="album-info">
                  <h3>Nombre del álbum 1</h3>
                  <button>Ver detalles</button>
                </div>
              </figure>
            </div>
          </div>


          <div class="column">
            <div class="gallery-item">
              <figure>
              <img src="https://images.unsplash.com/photo-1690983177044-943a605d301c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=729&q=80" onclick="openModal();currentSlide(3)">
              <div class="album-info">
                <h3>Nombre del álbum 1</h3>
                <button>Ver detalles</button>
              </div>
            </figure>
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
    position: relative;
  }

   .gallery-item img {
    width: 100%;
    height: auto;
    object-fit: cover;
  } 




  .album-info {
    position: absolute;
  bottom: 0; /* Colocar el texto y el botón en la parte inferior */
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 10px; /* Agregar un poco de espacio entre el texto y el botón */
  background-color: rgba(0, 0, 0, 0.7);
  color: white;
  opacity: 0;
  pointer-events: none;
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