from flask import Flask, render_template, request, jsonify
import os
import subprocess

app = Flask(__name__)

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle commands
@app.route('/command', methods=['POST'])
def handle_command():
    command = request.json.get('command')

    # Process the command and take appropriate actions
    if "open notepad" in command.lower():
        os.system("notepad.exe")
        response = "Opening Notepad"
    elif "open word" in command.lower():
        os.system("start winword")
        response = "Opening Word"
    elif "open excel" in command.lower():
        os.system("start excel")
        response = "Opening Excel"
    elif "close vs code" in command.lower():
        os.system("taskkill /IM Code.exe /F")
        response = "Closing VS Code"
    elif "minimise vs code" in command.lower():
        subprocess.run(["powershell", "-Command", "(Get-Process -Name 'Code').MainWindowHandle | ForEach-Object { [void] [User32]::ShowWindow($_, 2) }"])
        response = "Minimizing VS Code"
    else:
        response = f"Command '{command}' not recognized."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
