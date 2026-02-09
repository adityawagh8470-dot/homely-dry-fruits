document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("searchInput");
  if (!searchInput) return;

  searchInput.addEventListener("input", function () {
    const value = this.value.toLowerCase();

    /* ===== CART PAGE SEARCH ===== */
    const cartItems = document.querySelectorAll(".cart-item");
    if (cartItems.length > 0) {
      cartItems.forEach(item => {
        const nameEl = item.querySelector(".product-name");
        if (!nameEl) return;

        const name = nameEl.innerText.toLowerCase();
        item.style.display = name.includes(value) ? "flex" : "none";
      });
      return;
    }

    /* ===== PRODUCT PAGE SEARCH ===== */
    const products = document.querySelectorAll(".product-card");
    products.forEach(product => {
      const nameEl = product.querySelector(".product-name");
      if (!nameEl) return;

      const name = nameEl.innerText.toLowerCase();
      product.style.display = name.includes(value) ? "block" : "none";
    });
  });
});







