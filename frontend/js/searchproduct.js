window.addEventListener("load", function () {

  const searchInput = document.querySelector("#searchInput");

  if (!searchInput) {
    console.error("Search input not found!");
    return;
  }

  searchInput.addEventListener("input", function () {

    const value = this.value.toLowerCase();
    const products = document.querySelectorAll(".product-card");

    products.forEach(function (card) {

      const nameElement = card.querySelector(".product-name");

      if (!nameElement) return;

      const productName = nameElement.textContent.toLowerCase();

      if (productName.includes(value)) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }

    });

  });

});