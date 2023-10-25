
<script>
    import { onMount } from "svelte";
    import albums from '../albums'

import PhotoSwipeLightbox from 'photoswipe/lightbox';
import 'photoswipe/style.css';
export let galleryID;
export let images;


onMount(() => {
    let lightbox = new PhotoSwipeLightbox({
      gallery: '#' + galleryID,
      children: 'a',
      pswpModule: () => import('photoswipe'),
    });
    lightbox.init();})





    
</script>

<div class="pswp-gallery" id={galleryID}>
    {#each albums as album}
    <a
          href={album.cover}
          target="_blank"
          rel="noreferrer"
        >
          <img src={album.cover} alt="" />
          </a>
    {/each}
    </div>