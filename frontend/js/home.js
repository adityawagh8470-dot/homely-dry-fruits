function toggleMenu() {
  alert("Menu clicked!");
}

function toggleMenu() {
  var menu = document.getElementById("menu");
  if (menu.style.display === "block") {
    menu.style.display = "none";
  } else {
    menu.style.display = "block";
  }
}

function toggleMenu() {
  document.getElementById("sidebar").classList.toggle("active");
}




    // After login, store username
    

    const username = localStorage.getItem("username");
    const loginText = document.getElementById("loginText");
    const loginSection = document.getElementById("loginSection");

    if (username) {
        loginText.innerText = username;
    } else {
        loginSection.onclick = function () {
            window.location.href = "login.html";
        };
    }






   