const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatDisplay = document.getElementById('chat-display');

chatForm.addEventListener('submit', function (event) {
    event.preventDefault();
    const userMessage = userInput.value;
    appendMessage('User', userMessage);

    // Send user message to the server using AJAX/fetch
    fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `user_message=${encodeURIComponent(userMessage)}`,
    })
    .then(response => response.json())
    .then(data => {
        const chatbotResponse = data.response;
        appendMessage('Chatbot', chatbotResponse);
    })
    .catch(error => console.error('Error:', error));

    userInput.value = '';
});

function appendMessage(sender, message) {
    const messageDiv = document.createElement('div');
    messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatDisplay.appendChild(messageDiv);
    
    // Scroll the chat display to show the latest message
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
}
