<script>
  import {
    Lightbox,
    LightboxGallery,
    GalleryThumbnail,
    GalleryImage,
  } from "svelte-lightbox";
  import { ArrowLeftIcon} from 'svelte-feather-icons'
  import { onMount } from "svelte";
  import {location,pop} from 'svelte-spa-router'
  import Nav from "./Nav.svelte";
  let locacion
  let albumId;
  let album = [];

  locacion=$location
  albumId = locacion.split("/").pop();
  console.log(albumId)



  onMount(async () => {
        const [albumResponse] = await Promise.all([
          fetch(`http://127.0.0.1:8000/album/${albumId}`).then((response) => response.json()),
        ]);

        album = albumResponse;
        console.log(album)
  });






</script>


  <section class="section hero is-fullheight custom-component">
    <div class="container">
    <div class="columns is-2 is-multiline is-variable mt-6 ">
      
      <LightboxGallery>
        <svelte:fragment slot="thumbnail">
              <!-- <div class="column is-4"> -->
                {#if album && album.images && album.images.length > 0}
                  {#each album.images as image}
                  <div class="column is-2" >
                    <figure class="image is-flex  is-justify-content-center">
                <GalleryThumbnail>
                  <img src="{image.thumbnail}" alt="Simple lightbox" />
                </GalleryThumbnail>
              </figure>
              </div>

                  {/each}
                {:else}
                <p>No hay imágenes disponibles.</p>
                {/if}
        </svelte:fragment>
        

            {#if album && album.images && album.images.length > 0}
            {#each album.images as image}

            <GalleryImage>
              <img src="{image.picture}" alt="Simple lightbox" />
            </GalleryImage>
                {/each}
              {:else}
              <p>No hay imágenes disponibles.</p>
              {/if}
      </LightboxGallery>
    </div>
  </section>
