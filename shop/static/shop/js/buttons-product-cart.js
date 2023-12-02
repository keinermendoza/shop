function qunatityDown(id_product_quantity) {
    const quantityEl = document.getElementById(id_product_quantity);
    let currentQuantity = parseInt(quantityEl.value)
    if (currentQuantity > 1) {
        quantityEl.value = --currentQuantity;
    } 
}

function quantityUp(id_product_quantity) {
    const quantityEl = document.getElementById(id_product_quantity);
    let currentQuantity = parseInt(quantityEl.value)
    quantityEl.value =  ++currentQuantity;
}