// Getting references to the elements
const commandInput = document.getElementById('commandInput');
const sendCommandBtn = document.getElementById('sendCommandBtn');
const voiceCommandBtn = document.getElementById('voiceCommandBtn');
const historyBtn = document.getElementById('historyBtn');
const settingsBtn = document.getElementById('settingsBtn');
const historyModal = document.getElementById('historyModal');
const settingsModal = document.getElementById('settingsModal');
const closeButtons = document.querySelectorAll('.close');

// Command history
let commandHistory = [];

// Send button handler
sendCommandBtn.addEventListener('click', function() {
    const command = commandInput.value.trim();
    if (command) {
        processCommand(command);
        commandHistory.push(command);
        commandInput.value = ''; // Clear input after sending
    }
});

// Voice command button (using Web Speech API)
voiceCommandBtn.addEventListener('click', function() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.start();

    recognition.onresult = function(event) {
        const voiceCommand = event.results[0][0].transcript;
        processCommand(voiceCommand);
        commandHistory.push(voiceCommand);
    };

    recognition.onerror = function(event) {
        console.error("Error occurred during voice recognition: ", event.error);
    };
});

// Process commands and interact with main.py backend
function processCommand(command) {
    console.log("Processing command: ", command);
    // Here you will send the command to the backend (e.g., using AJAX or WebSockets)
}

// Show history modal
historyBtn.addEventListener('click', function() {
    historyModal.style.display = 'flex';
    const historyContent = document.getElementById('historyContent');
    historyContent.innerHTML = commandHistory.join('<br>');
});

// Show settings modal
settingsBtn.addEventListener('click', function() {
    settingsModal.style.display = 'flex';
});

// Close modals
closeButtons.forEach(button => {
    button.addEventListener('click', function() {
        historyModal.style.display = 'none';
        settingsModal.style.display = 'none';
    });
});

// Process commands and interact with Flask backend
function processCommand(command) {
    console.log("Processing command: ", command);
    
    // Send the command to the Flask backend using AJAX
    fetch('/command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ command: command }),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.response);  // Display backend response to user
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
