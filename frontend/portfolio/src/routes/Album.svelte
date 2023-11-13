<script>
  import {
    Lightbox,
    LightboxGallery,
    GalleryThumbnail,
    GalleryImage,
  } from "svelte-lightbox";
  import { onMount } from "svelte";
  import { getContext } from "svelte";
  import { each } from "svelte/internal";


let albumId=7;
let album = [];


  onMount(async () => {
    try {
      const [albumResponse] = await Promise.all([
        fetch(`http://127.0.0.1:8000/album/${albumId}`).then((response) => response.json()),
      ]);

      album = albumResponse;
      console.log(album);  // Asegúrate de que estás viendo las imágenes específicas del álbum en la consola
    } catch (error) {
      console.error(error);
    }
  });






</script>

  <section class="section">
    <div class="columns is-4 is-multiline">
      <LightboxGallery>
        <svelte:fragment slot="thumbnail">
              <div class="column is-2">
                {#if album && album.images && album.images.length > 0}
                {#each album.images as image}
                <GalleryThumbnail>
                  <img src="{image.thumbnail}" alt="Simple lightbox" />
                </GalleryThumbnail>
                {/each}
                {:else}
                <p>No hay imágenes disponibles.</p>
                {/if}
              </div>
        </svelte:fragment>

            <GalleryImage>
              <img src="" alt="Simple lightbox" />
            </GalleryImage>
      </LightboxGallery>
    </div>
  </section>
