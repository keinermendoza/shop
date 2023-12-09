document.addEventListener("htmx:confirm", function(e) {
    if (Array.from(e.target.classList).includes('delete-btn'))  { 
        e.preventDefault()
  
      // Mostrar un cuadro de diálogo personalizado con Swal
      Swal.fire({
        title: "Proceed?",
        text: `I ask you... ${e.detail.question}`
      }).then(function(result) {
        if (result.isConfirmed) {
   
            console.log('adentro del wsal')
            e.detail.issueRequest(true); 

            const event = new CustomEvent("deleterow", {detail : {itemId : e.target.dataset.rowid}});
            window.dispatchEvent(event);

        }
      });
    }
  });


document.addEventListener('alpine:init', () => {
  Alpine.store('cart', {
    items: [],
    totalPrice: 0,
    countItems: 0,

    getTotalPrice(n) {
      this.totalPrice = parseFloat(n).toFixed(2);
    },
    getCountItems(n) {
      this.countItems = parseInt(n);
    },
    updateTotals() {
        this.countItems = this.items.reduce((sum, item) => sum + item.quantity, 0);
        this.totalPrice = (this.items.reduce((sum, item) => sum + item.quantity * item.price, 0)).toFixed(2)
    },

    updateItemQuantity(newQuantity, itemId) {
      this.items[this.items.findIndex(item => item.id === itemId)].quantity = newQuantity;
      this.updateTotals();
    },

    deleteItem(itemId) {
      this.items = this.items.filter(item => item.id != itemId);
      this.updateTotals();
    }

  })

})