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

<div class="columns is-multiline" style="outline: 2px solid red;">

<LightboxGallery>
    <svelte:fragment slot="thumbnail">
        {#each albums as album}
        <div class="column is-4 " >
            <GalleryThumbnail>
                <img src="{album.thumbnailURL}" alt="Simple lightbox">
            </GalleryThumbnail>
        </div>
        {/each}

        
    </svelte:fragment>
    
    <GalleryImage>
        <img src="./image-0.jpg" alt="Simple lightbox">
    </GalleryImage>
    <GalleryImage>
        <img src="./image-1.jpg" alt="Simple lightbox">
    </GalleryImage>
    <GalleryImage>
        <img src="./image-2.jpg" alt="Simple lightbox">
    </GalleryImage>
</LightboxGallery>
</div>

</section>