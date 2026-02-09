const BASE_URL = "http://127.0.0.1:8000/api";

function getToken() {
  return localStorage.getItem("access");
}

async function placeOrder() {
  const token = getToken();

  if (!token) {
    alert("❌ Please login first");
    throw "No token";
  }

  const response = await fetch(`${BASE_URL}/orders/place/`, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json"
    }
  });

  if (!response.ok) {
    const err = await response.text();
    console.error("ORDER API ERROR:", err);
    throw err;
  }

  return await response.json();
}
