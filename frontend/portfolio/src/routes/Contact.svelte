<script>
    import { SendIcon } from 'svelte-feather-icons'

    // import Animate from "./Animate.svelte";
    import { onMount } from "svelte";





    

//     let message;
//     let email;
//     let contacts = [];

//   onMount(async () => {
//     fetch("https://vic.uy/contact/")
//       .then((response) => response.json())
//       .then((data) => {
//         contacts = data;
//         console.log(contacts);
//         // console.log(data);
//       })
//       .catch((error) => {
//         // console.log(error);
//         return [];
//       });
//   });

  
//   function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;

// }




//   const sendEmail=async () => {

//     const csrfCookie = getCookie("csrftoken");

//     const recaptchaResponse = grecaptcha.getResponse();

//     const response = await fetch("https://vic.uy/send_email/", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//         "X-CSRFToken": csrfCookie, 
//       },
//       body: JSON.stringify({ message, email,recaptchaResponse }),
//       credentials: 'include',
//     });

//     if (!response.ok) {
//       console.log(response)
//       const data = await response.json();
//       console.error("Error enviando correo",data);
//       document.getElementById("message").textContent = "Error al enviar e mensaje, intentelo nuevamente";

//     } else {
//       console.log(response)

//       // const data = await response.json();
//       document.getElementById("message").textContent = "Mensaje enviado con exito";

//       console.log("Correo enviado correctamente");
//     }
//   };




//   let recaptchaResponse = null;

// function onRecaptcha(response) {
//   recaptchaResponse = response;
// }


</script>
      <section class="section">
    <div class="columns is-multiline mx-2 my-6">
      <div class="column"></div>
      <div class="column is-one-third">
        <div class="container">

          <h4 class="title custom-title"></h4>
          <p class="custom-text"></p>
          <div class="custom-message" id="message"></div>

        </div>
        <form class="form-contact" action="" >
          <div class="title">Contact</div>
        <div class="field">
          <label class="label custom-label">Email</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input custom-input " type="email" placeholder="Email input">
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-exclamation-triangle"></i>
            </span>
          </div>
        </div>
      

        <div class="field">
          <label class="label custom-label">Message</label>
          <div class="control">
            <textarea class="textarea custom-input"   placeholder="Message"></textarea>
          </div>
        </div>

        <div class="field is-grouped is-justify-content-center">
          <div class="control btn-cv  ">
            <button class="button custom-button  is-normal is-rounded ">
              <span>
              <SendIcon size="24" />
            </span>
              Send</button>
          </div>

        </div>

      </form>
      <div class="column">
      <div class="container">
      <div class="g-recaptcha " data-sitekey="6Ld7NskkAAAAAJKzdpVtsTXKBUdX_TT3dizQHxA8"></div>

      <script src="https://www.google.com/recaptcha/api.js" async defer></script>
    </div>
  </div>
      </div>

      <div class="column"></div>
      <script src="https://www.google.com/recaptcha/api.js" async defer></script>

    </div>

  </section>






  <style>


  




.title {
  font-family:'Montserrat', sans-serif;
    text-align: center;
    color: #2d334a;
  }

  .title-section{
  font-family: 'Montserrat', sans-serif;
  font-size: 2.6rem;
  text-align: center;

}



.custom-title{
  color:#0f0e17;
  text-align: center;
}



.custom-button{
  background-color: #6246ea;
    border: none;
    color: #fffffe;
    width: 105px;
    margin-bottom: 36px;
    margin-top: 36px;

}





.custom-input{
border-color:#1f1235 ;
}


.custom-label{
  color: #1f1235;
  

}
.custom-text{
  text-align: justify;
  color: #1f1235;
  font-family: "Inconsolata", monospace;
  line-height: 1.70rem;
}


.custom-message{
  color: green;
  text-align: center;
}


.g-recaptcha{
  margin: 0 auto;
  width: 304px;
}

button:hover:before {
  opacity: 0.2;
}

button:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.form-contact{
  background-color: #d1d1e9;
  padding: 50px;
  background: #fffffe;
  box-shadow:  20px 20px 60px #d9d9d8,
              -20px -20px 60px #ffffff;
              border-radius: 5px;

}
  </style>