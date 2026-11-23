/* ===== CHATBOT ===== */

function toggleChat() {
  let bot = document.getElementById("chatbot");

  if (bot.style.display === "flex") {
    bot.style.display = "none";
  } else {
    bot.style.display = "flex";
  }
}

function askProduct(product) {
  document.getElementById("user-input").value = "Tell me about " + product;

  sendMessage();
}

async function sendMessage() {
  let input = document.getElementById("user-input");
  let message = input.value;

  if (message.trim() === "") return;

  let chat = document.getElementById("chat-body");

  chat.innerHTML += `<p><b>You:</b> ${message}</p>`;

  input.value = "";

  try {
    let response = await fetch("http://127.0.0.1:8000/api/chatbot/chat/", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        message: message,
      }),
    });

    let data = await response.json();

    chat.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;
  } catch (error) {
    chat.innerHTML += `<p style="color:red"><b>Bot:</b> Server error</p>`;
  }

  chat.scrollTop = chat.scrollHeight;
}

document
  .getElementById("user-input")
  .addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      sendMessage();
    }
  });