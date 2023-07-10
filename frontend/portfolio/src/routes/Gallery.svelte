<script>
    import Gallery from 'svelte-image-gallery'
    import { onMount } from "svelte";
    function handleClick(e) {
		console.log(e.detail.src)
	}
</script>
<section class="hero is-fullheight custom-component mt-6">
    <div class="columns" >
        <div class="column"></div>
        <div class="column is-four-fifths">
            <h2 class="title">Photo</h2>
    <Gallery  gap="30" maxColumnWidth="400" on:click={handleClick} >
        <div class="efect-img">
            <img  src="https://images.unsplash.com/photo-1686208303474-31237e3ec4f3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=735&q=80" />
            <div class="image-over">
                <h3 class="title"></h3>
                <a class="btn-go-to-album" href="">Album</a>
            </div>
        </div>
        <img class="efect-img" src="https://images.unsplash.com/photo-1686237542774-4f1ead43a6d6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=846&q=80" />
        <img class="efect-img" src="https://images.unsplash.com/photo-1686214715439-44ad1b59e0ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=695&q=80" />
        <img class="efect-img" src="https://images.unsplash.com/photo-1685977706328-7db7f86db70d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="">
        <img class="efect-img" src="https://images.unsplash.com/photo-1686176940284-15fcae290283?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=671&q=80" alt="">
        <img class="efect-img" src="https://images.unsplash.com/photo-1686131128954-3ceccda2d684?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=735&q=80" alt="">
        <img class="efect-img" src="https://images.unsplash.com/photo-1685983633468-bf187eca26ad?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=764&q=80" alt="">
        <img class="efect-img" src="https://images.unsplash.com/photo-1601895905331-5c877f444583?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80" alt="">
    </Gallery>
</div>
<div class="column"></div>


</div>
</section>

<style>

.efect-img {
    opacity: 0.9;
    transition: all 0.2s;
}

.efect-img:hover {
    opacity: 1;
    transform: scale(1.04);
}


.title{
font-family: 'Montserrat', sans-serif;
font-size: 2.6rem;
    }

.image-over{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    opacity: 0 ;
    background-color: rgba(0, 0, 0, 0.8);
    transition: opacity 0.2s;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.efect-img:hover .image-over {
  opacity: 1;
}

.image-title {
  color: #fff;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.btn-go-to-album {
  background-color: #fff;
  color: #000;
  padding: 0.5rem 1rem;
  text-decoration: none;
  font-weight: bold;
}


</style>