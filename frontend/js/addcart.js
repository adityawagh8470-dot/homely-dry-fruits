// 1. The Single Source of Truth for updating the UI
function updateCartUI() {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const count = cart.reduce((sum, item) => sum + item.qty, 0);
  
  const span = document.getElementById("cart-count");
  if (span) {
    span.innerText = count;
    // Optional: Add a little animation so the user notices the change
    span.classList.add('bump'); 
    setTimeout(() => span.classList.remove('bump'), 300);
  }
}

// 2. The logic to handle button clicks
const addButtons = document.querySelectorAll(".add-to-cart");

addButtons.forEach(btn => {
  btn.addEventListener("click", () => {

    const name = btn.dataset.name;
    const basePrice = parseFloat(btn.dataset.price);
    const card = btn.closest(".product-card");
    const image = card.querySelector("img").src;
    const size = 500;

    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    const existing = cart.find(item =>
      item.name === name && item.size === size
    );

    if (existing) {
      alert("Product already added to cart!");
      return;  
    }

    cart.push({
      name,
      basePrice,
      image,
      size,
      qty
    });

    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartCount();
  });
});
// 3. Initialize on page load
document.addEventListener("DOMContentLoaded", updateCartUI);


// Change "updateCartUI" to "updateCartCount" to match common.js
addButtons.forEach(btn => {
  btn.addEventListener("click", () => {
    // ... (your existing logic to add to cart) ...

    localStorage.setItem("cart", JSON.stringify(cart));
    
    updateCartCount(); // ✅ Matches the function in common.js
    alert(`${name} added to cart!`);
  });
});