document.addEventListener("htmx:confirm", function(e) {
    if (Array.from(e.target.classList).includes('delete-btn'))  { 
        e.preventDefault()
  
      // Mostrar un cuadro de diálogo personalizado con Swal
      Swal.fire({
        title: "Proceed?",
        text: `I ask you... ${e.detail.question}`
      }).then(function(result) {
        // Si el usuario confirma, continuar con la solicitud htmx
        if (result.isConfirmed) {
            // const deleteItemData = new CustomEvent('deleteItemData', {detail : 'hola desde el custom event'})
            // window.dispatchEvent(deleteItemData)
            console.log('adentro del wsal')
            e.detail.issueRequest(true); 


            // cuando uso simple event con add eventlistener vanilla funciona
            // la version vanilla del custom event tambien funciona

            const event = new CustomEvent("deleterow", {detail : {id : e.target.dataset.rowid}});
            window.dispatchEvent(event);

            // Dispatch the event.
        }
      });
    }
  });

  // const event = new CustomEvent("build", { detail: elem.dataset.time });

// document.addEventListener('DOMContentLoaded', () => {
 

// // Listen for the event.
// window.addEventListener(
//   "hello",
//   (e) => {
//     console.log('hola', e.detail.id)
//   },
//   false,
// );


// })