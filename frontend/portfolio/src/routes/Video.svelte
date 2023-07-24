<script>
    import { onMount } from "svelte";
    function handleClick(e) {
		console.log(e.detail.src)
	}
</script>
<section class="section">
    <div class="container">
      <div class="columns is-multiline">
         
         
          <div class="column is-4">
            <div class="gallery-item box" data-index="">
              <figure class="image is-square">
                <video src="../../video/istockphoto-1175207653-640_adpp_is.mp4"></video>
               
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

    .gallery-item {
    cursor: pointer;
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
    background-color: #ff5722;
    color: white;
    border: none;
    cursor: pointer;
  }


  video {
    width: 100%;
  }
</style>