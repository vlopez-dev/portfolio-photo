
<script>
  import { onMount } from "svelte";

let about = [];
onMount(async () => {
    try{
      const[aboutResponse] = await Promise.all([
        fetch("http://127.0.0.1:8000/about/").then((response) => response.json()),
      ]);
      about = aboutResponse;
      console.log(about)
    }catch(error){
      console.log(error);
    }
  });

</script>




<section class="section hero is-fullheight custom-component">
    {#each about as about}
    
    <div class="container">
        <h2 class="title title-section">About me</h2>
    </div>
<div class="columns is-multiline mx-2 my-6" >
    
    <div class="column" ></div>
    <div class="column is-one-third" >
        <figure class="is-flex is-justify-content-center ">
        <img class="is-rounded about-image-shadow" src={about.image} alt="">
    </figure>
</div>
    <div class="column" >
        <div class="container">
            <h2 class="title title-about">{about.title}</h2>
            <p class="subtitle paragraff-about">{about.description}</p>
        </div>
    </div>
    <div class="column" ></div>

</div>
{/each}

</section>


<style>
   img{
    width: 60%;
    height: auto;
    /* border-radius: 50%; */
   }

   .title-section{
  font-family: 'Montserrat', sans-serif;
  font-size: 2.6rem;
  text-align: center;

}


   .about-image-shadow{
    box-shadow: 0 30px 30px -30px rgba(27, 26, 26, 0.315);

   }

   figure{
    background-color: #d1d1e9;
    border-radius: 3% 97% 0% 100% / 0% 99% 1% 100% ;
    /* fancyborder */
   }


   .title-about{
    font-family:'Montserrat', sans-serif;
;
   }

   .paragraff-about{
    font-family: 'Hind', sans-serif;
   }
</style>