<script>
  import {
    Lightbox,
    LightboxGallery,
    GalleryThumbnail,
    GalleryImage,
  } from "svelte-lightbox";
  import { onMount } from "svelte";
  import {location, querystring} from 'svelte-spa-router'
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
    <div class="columns is-4 is-multiline">
      <LightboxGallery>
        <svelte:fragment slot="thumbnail">
              <!-- <div class="column is-4"> -->
                {#if album && album.images && album.images.length > 0}
                  {#each album.images as image}
                  <div class="column is-4">

                <GalleryThumbnail>
                  <img src="{image.thumbnail}" alt="Simple lightbox" />
                </GalleryThumbnail>
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
