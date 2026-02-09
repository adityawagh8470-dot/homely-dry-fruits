const cartItemsDiv = document.getElementById("cart-items");
const cartTotalSpan = document.getElementById("cart-total");

function renderCart() {
  let cart = JSON.parse(localStorage.getItem("cart")) || [];
  cartItemsDiv.innerHTML = "";

  if (cart.length === 0) {
    cartItemsDiv.innerHTML = "<p class='text-center'>Your cart is empty</p>";
    cartTotalSpan.innerText = "₹0";
    return;
  }

  let total = 0;

  cart.forEach((item, index) => {
    const itemPrice = (item.basePrice / 500) * item.size;
    const itemTotal = itemPrice * item.qty;
    total += itemTotal;

    const div = document.createElement("div");
    div.className = "row border p-2 mb-2";

    div.innerHTML = `
      <div class="col-md-2">
        <img src="${item.image}" class="img-fluid" style="max-height:80px">
      </div>
      <div class="col-md-3">
        <strong>${item.name}</strong><br>
        ₹${itemPrice.toFixed(2)} / ${item.size}g
      </div>
      <div class="col-md-2">
        <input type="number" min="1" value="${item.qty}" 
          class="form-control qty" data-index="${index}">
      </div>
      <div class="col-md-2">
        <strong>₹${itemTotal.toFixed(2)}</strong>
      </div>
      <div class="col-md-2">
        <select class="form-select size" data-index="${index}">
          <option value="100" ${item.size==100?"selected":""}>100g</option>
          <option value="250" ${item.size==250?"selected":""}>250g</option>
          <option value="500" ${item.size==500?"selected":""}>500g</option>
          <option value="1000" ${item.size==1000?"selected":""}>1kg</option>
        </select>
      </div>
      <div class="col-md-1">
        <button class="btn btn-danger btn-sm remove" data-index="${index}">
          ✖
        </button>
      </div>
    `;

    cartItemsDiv.appendChild(div);
  });

 
  cartTotalSpan.innerText = `₹${total.toFixed(2)}`;
localStorage.setItem("price", total.toFixed(2)); // ✅ ADD THIS


  // Quantity change
  document.querySelectorAll(".qty").forEach(input => {
    input.addEventListener("change", e => {
      cart[e.target.dataset.index].qty = parseInt(e.target.value) || 1;
      localStorage.setItem("cart", JSON.stringify(cart));
      renderCart();
    });
  });

  // Size change
  document.querySelectorAll(".size").forEach(select => {
    select.addEventListener("change", e => {
      cart[e.target.dataset.index].size = parseInt(e.target.value);
      localStorage.setItem("cart", JSON.stringify(cart));
      renderCart();
    });
  });

  // Remove
  document.querySelectorAll(".remove").forEach(btn => {
    btn.addEventListener("click", e => {
      cart.splice(e.target.dataset.index, 1);
      localStorage.setItem("cart", JSON.stringify(cart));
      renderCart();
    });
  });
}

renderCart();




function addToCart(itemId) {
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(itemId); // or store quantity & item details
    localStorage.setItem('cart', JSON.stringify(cart));

    updateCartCount();
}


// ... inside renderCart() function ...

// Update Quantity
document.querySelectorAll(".qty").forEach(input => {
  input.addEventListener("change", e => {
    cart[e.target.dataset.index].qty = parseInt(e.target.value) || 1;
    localStorage.setItem("cart", JSON.stringify(cart));
    renderCart();
    updateCartCount(); // ✅ Add this
  });
});

// Remove Item
document.querySelectorAll(".remove").forEach(btn => {
  btn.addEventListener("click", e => {
    cart.splice(e.target.dataset.index, 1);
    localStorage.setItem("cart", JSON.stringify(cart));
    renderCart();
    updateCartCount(); // ✅ Add this
  });
});