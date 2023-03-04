window.addEventListener("DOMContentLoaded", () => {
  const messages = document.getElementById("mensajes");    
  const websocket = new WebSocket("wss://5678-karenxiomar-entregadelo-3owpm4nl5p0.ws-us89.gitpod.io/");
  
  websocket.onmessage = ({ data }) => {
    const message = document.createElement("li");
    const content = document.createTextNode(data);
    message.appendChild(content);
    messages.appendChild(message);
  };
});