document.addEventListener("DOMContentLoaded", () => {
  // Load Navbar
  fetch("./navbar.html")
    .then(res => {
      if (!res.ok) throw new Error("Navbar not found");
      return res.text();
    })
    .then(html => {
      document.getElementById("navbar").innerHTML = html;
      // ✅ CRITICAL: Update the count ONLY after the navbar exists in the DOM
      updateCartCount(); 
    })
    .catch(err => console.error("Navbar error:", err));

  // Load Footer
  fetch("./footer.html")
    .then(res => res.text())
    .then(html => {
      document.getElementById("footer").innerHTML = html;
    });
});

// Use this name consistently across ALL files
function updateCartCount() {
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const count = cart.reduce((sum, item) => sum + item.qty, 0);
  const span = document.getElementById("cart-count");
  
  if (span) {
    span.innerText = count;
  }
}

document.addEventListener("DOMContentLoaded", function () {
    const navbarDiv = document.getElementById("navbar");
    if (navbarDiv) {
        navbarDiv.innerHTML = `
            <nav class="navbar">
                <div class="nav-left">
                    <h2>Homely</h2>
                </div>
                <div class="nav-center">
                    <input type="text" id="searchInput" placeholder="Search dry fruits...">
                </div>
                <div class="nav-right">
                    <button class="nav-btn">Login / Signup</button>
                    <div class="cart-container">
                        <a href="./cart.html" class="cart-link">
                            <i class="fa-solid fa-cart-shopping"></i> <span id="cart-count">0</span>
                        </a>
                    </div>
                </div>
            </nav>
        `;
    }

    // Logic to update cart count from localStorage
    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const countElement = document.getElementById("cart-count");
    if (countElement) {
        countElement.innerText = cart.length;
    }
});