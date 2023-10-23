 <script>
    import { 
        Lightbox,
        LightboxGallery,
        GalleryThumbnail,
        GalleryImage
    } from 'svelte-lightbox'
    
    let lightboxProgrammaticController
 </script>
 <LightboxGallery>
    <!-- Layout-->
    <svelte:fragment slot="thumbnail">
        <div class="sample-class-1">
            <GalleryThumbnail>
                <img src="https://unsplash.com/es/fotos/una-gran-formacion-rocosa-con-un-pequeno-agujero-en-el-medio-de-ella-_jfejQo2tZw" alt="Simple lightbox">
            </GalleryThumbnail>
            <div class="sample-class-2">
                <div class="sample-class-3">
                    <img src="https://unsplash.com/es/fotos/una-gran-formacion-rocosa-con-un-pequeno-agujero-en-el-medio-de-ella-_jfejQo2tZw" alt="Simple lightbox">
                </div>
                <div class="sample-class-4">
                    <img src="./thumbnail-0.jpg" alt="Simple lightbox">
                </div>
            </div>
        </div>
    </svelte:fragment>
    
    <GalleryImage>
        <img src="https://images.unsplash.com/photo-1682685797736-dabb341dc7de?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Simple lightbox">
    </GalleryImage>
    <GalleryImage>
        <img src="./image-1.jpg" alt="Simple lightbox">
    </GalleryImage>
    <GalleryImage>
        <img src="./image-2.jpg" alt="Simple lightbox">
    </GalleryImage>
</LightboxGallery>