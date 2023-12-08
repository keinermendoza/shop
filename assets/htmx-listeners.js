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
            let deleteItemData = new CustomEvent('deleteItemData', {detail : {rowid: e.target.dataset.rowid}})
            window.dispatchEvent(deleteItemData)

            e.detail.issueRequest(true); 
        }
      });
    }
  });