<script>
     import { 
        Lightbox,
        LightboxGallery,
        GalleryThumbnail,
        GalleryImage
    } from 'svelte-lightbox'
    
    let lightboxProgrammaticController
    import albums from '../albums'

</script>


<section class="section">

<div class="columns  is-4 is-multiline " >

<LightboxGallery>
    <svelte:fragment slot="thumbnail">
        {#each albums as album}
        {#each album.imagenes as imagen}
        <div class="column is-2 " >
            <GalleryThumbnail>
                <img src="{imagen.thumbnailURL}" alt="Simple lightbox">
            </GalleryThumbnail>
        </div>
        {/each}

        {/each}

        
    </svelte:fragment>
    {#each albums as album}
    {#each album.imagenes as imagen}

   
    <GalleryImage>
        <img src="{imagen.imageurl}" alt="Simple lightbox">
    </GalleryImage>
    {/each}

    {/each}

</LightboxGallery>
</div>

</section>