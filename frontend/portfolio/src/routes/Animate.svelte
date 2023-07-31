<script>
    import {blur} from 'svelte/transition'
</script>

<div transition:slide={{ delay: 200 }} >
    <slot />
</div> 

<style>
   
</style>