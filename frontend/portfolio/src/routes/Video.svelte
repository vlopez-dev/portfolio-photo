<script>

    import { onMount } from "svelte";
    function handleClick(e) {
		console.log(e.detail.src)
	}
let videos=[];

  onMount(async () => {
    try{
      const[videoResponse] = await Promise.all([
        fetch("http://127.0.0.1:8000/video/").then((response) => response.json()),
      ]);
      videos = videoResponse;
      console.log(videos)
    }catch(error){
      console.log(error);
    }
  });


</script>
<section class="section ">
    <div class="container">
      <h2 class="title title-section ">Video</h2>
      <div class="columns is-multiline">
         {#each videos as video}

          <div class="column is-4">
            <div class="gallery-item " data-index="">
                <video controls autoplay >
                  <source src="{video.video}">
                </video>
               
            </div>
          </div>
          {/each}

       
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
    background-color: #ff5722;
    color: white;
    border: none;
    cursor: pointer;
  }


  video {
    width: 100%;
  }

  .gallery-item {
    cursor: pointer;
  }

  .gallery-item video {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>