
<script>

import { onMount } from 'svelte';
	import lightGallery from 'lightgallery';
	import lgThumbnail from 'lightgallery/plugins/thumbnail';
	import lgZoom from 'lightgallery/plugins/zoom';

	lightGallery(document.getElementById('lightgallery'), {
			plugins: [lgZoom, lgThumbnail],
			speed: 500,
			licenseKey: 'your_license_key'
		});

</script>

<div id="lightgallery">
    <a href="https://images.unsplash.com/photo-1682685797857-97de838c192e?auto=format&fit=crop&q=80&w=1974&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" data-lg-size="1600-2400">
        <img alt=".." src="https://images.unsplash.com/photo-1682685797857-97de838c192e?auto=format&fit=crop&q=60&w=500&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHx8" />
    </a>
    <a href="https://plus.unsplash.com/premium_photo-1674086619163-54bd6379f538?auto=format&fit=crop&q=80&w=1975&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" data-lg-size="1024-800">
        <img alt=".." src="https://plus.unsplash.com/premium_photo-1674086619163-54bd6379f538?auto=format&fit=crop&q=60&w=500&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwyfHx8ZW58MHx8fHx8" />
    </a>

    <a href="https://images.unsplash.com/photo-1697949314141-584b03d2ecd5?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" data-lg-size="1600-2400">
        <img alt=".." src="https://images.unsplash.com/photo-1697949314141-584b03d2ecd5?auto=format&fit=crop&q=60&w=500&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw4fHx8ZW58MHx8fHx8" />
    </a>

    <a href="https://plus.unsplash.com/premium_photo-1695822019130-29e68d5b2d6d?auto=format&fit=crop&q=80&w=2070&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">
        <img alt=".." src="https://plus.unsplash.com/premium_photo-1695822019130-29e68d5b2d6d?auto=format&fit=crop&q=60&w=500&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwxN3x8fGVufDB8fHx8fA%3D%3D" />
    </a>
</div>