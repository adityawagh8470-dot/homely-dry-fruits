const loginForm = document.getElementById("loginForm");
const registerForm = document.getElementById("registerForm");
const formTitle = document.getElementById("formTitle");

const loginUsernameInput = document.getElementById("loginUsername");
const loginPasswordInput = document.getElementById("loginPassword");

const firstNameInput = document.getElementById("firstName");
const lastNameInput = document.getElementById("lastName");
const regEmailInput = document.getElementById("regEmail");
const regPasswordInput = document.getElementById("regPassword");
const confirmPasswordInput = document.getElementById("confirmPassword");

function showRegister() {
  loginForm.style.display = "none";
  registerForm.style.display = "block";
  formTitle.innerText = "Create Account";
}

function showLogin() {
  registerForm.style.display = "none";
  loginForm.style.display = "block";
  formTitle.innerText = "Login";
}

/* LOGIN */
loginForm.addEventListener("submit", async function (e) {
  e.preventDefault();

  const username = loginUsernameInput.value.trim();
  const password = loginPasswordInput.value.trim();

  if (!username || !password) {
    alert("All fields required");
    return;
  }

  // Frontend Warning: Check for email address usage
  if (username.includes("@")) {
    const confirmLogin = confirm(
      "You entered an email address. This system requires your username (usually the part before @). " +
      "Do you want to try continuing with '" + username + "' anyway?"
    );
    if (!confirmLogin) return;
  }

  console.log("Attempting login with username:", username);

  try {
    const res = await fetch("http://127.0.0.1:8000/api/auth/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: username,
        password: password
      })
    });

    const data = await res.json();
    console.log("Login User Response:", data);

    if (!res.ok) {
      let msg = data.detail || "Login failed";

      // Provide a smart hint if they likely used the wrong username
      if (msg.includes("No active account") && username.includes("@")) {
        msg += "\n\nHINT: You used an email address. Try using your username instead (e.g. if your email is john@example.com, try 'john').";
      }
      alert(msg);
      return;
    }

    localStorage.setItem("access", data.access);
    localStorage.setItem("refresh", data.refresh);

    alert("Login successful!");
    window.location.href = "index.html";
  } catch (err) {
    console.error("Login Error:", err);
    alert("Network error. Please make sure the backend server is running on port 8000.");
  }
});

/* REGISTER */
registerForm.addEventListener("submit", async function (e) {
  e.preventDefault();

  const fn = firstNameInput.value.trim();
  const ln = lastNameInput.value.trim();
  const email = regEmailInput.value.trim();
  const pass = regPasswordInput.value.trim();
  const cpass = confirmPasswordInput.value.trim();

  if (!fn || !ln || !email || !pass || !cpass) {
    alert("All fields required");
    return;
  }

  if (pass !== cpass) {
    alert("Passwords do not match");
    return;
  }

  try {
    const res = await fetch("http://127.0.0.1:8000/api/auth/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username: email.split("@")[0],
        email: email,
        password: pass,
        first_name: fn,
        last_name: ln
      })
    });

    const data = await res.json();

    if (!res.ok) {
      alert(data.error || "Registration failed");
      return;
    }

    alert("Account created successfully. Please login.");
    showLogin();
  } catch (err) {
    console.error(err);
    alert("Network error or server is down.");
  }
});
