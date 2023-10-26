
<script>
    import { onMount } from "svelte";
    import albums from '../albums'

import PhotoSwipeLightbox from 'photoswipe/lightbox';
import 'photoswipe/style.css';
export let galleryID;


onMount(() => {
    let lightbox = new PhotoSwipeLightbox({
      gallery: '#' + galleryID,
      children: 'a',
      showHideAnimationType: 'zoom',
      pswpModule: () => import('photoswipe'),
    });

    lightbox.on('uiRegister', function() {
  lightbox.pswp.ui.registerElement({
    name: 'test-button',
    ariaLabel: 'Toggle zoom',
    order: 9,
    isButton: true,
    html: 'Test',
    onClick: (event, el) => {
      if ( confirm('Do you want to toggle zoom?') ) {
        lightbox.pswp.toggleZoom();
      }
    }
  });
});
    lightbox.init();})





    
</script>
<div class="section">
  <div class="columns">
    <div class="column">
      <div  class="pswp-gallery" id={galleryID}>
        {#each albums as album}
        <a
              href={album.cover}
              
              data-pswp-width={album.width}
              data-pswp-height={album.height}
              target="_blank"
              rel="noreferrer"
            >
              <img src="{album.thumbnailURL}" alt="" />
              </a>
        {/each}
        </div>
    </div>
  </div>
</div>



<style></style>