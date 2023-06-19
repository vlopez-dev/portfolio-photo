<script>
    import Gallery from 'svelte-image-gallery'
    import { onMount } from "svelte";
    function handleClick(e) {
		console.log(e.detail.src)
	}
</script>
<section class="m-6">
<Gallery  gap="30" maxColumnWidth="400" on:click={handleClick} >
	<img src="https://images.unsplash.com/photo-1686208303474-31237e3ec4f3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=735&q=80" />
	<img src="https://images.unsplash.com/photo-1686237542774-4f1ead43a6d6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=846&q=80" />
    <img src="https://images.unsplash.com/photo-1686214715439-44ad1b59e0ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=695&q=80" />
    <img src="https://images.unsplash.com/photo-1685977706328-7db7f86db70d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="">
    <img src="https://images.unsplash.com/photo-1686176940284-15fcae290283?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=671&q=80" alt="">
    <img src="https://images.unsplash.com/photo-1686131128954-3ceccda2d684?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=735&q=80" alt="">
    <img src="https://images.unsplash.com/photo-1685983633468-bf187eca26ad?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=764&q=80" alt="">
    <img src="https://images.unsplash.com/photo-1601895905331-5c877f444583?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="">
</Gallery>
</section>

<style>
    :global(img) { opacity: .9; transition: all .2s }
	:global(img):hover { opacity: 1; transform: scale(1.04) }


    img{
        border-radius: 38px;
background: #e3f6f5;
box-shadow:  15px 15px 30px #c1d1d0,
             -15px -15px 30px #ffffff;
    }
</style>