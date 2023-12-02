document.addEventListener("htmx:confirm", function(e) {
    e.preventDefault()

    Swal.fire({
        title: "Are you sure?",
        text: `${e.detail.question}`,
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Remove it!"
      }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Removed!",
                icon: "success"
            }).finally(() => {
                e.detail.issueRequest(true)
            });
            
        }
        
      })

  })