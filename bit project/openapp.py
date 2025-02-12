import os
import subprocess
import pygetwindow as gw

# Function to open applications based on voice commands
def open_application(app_name):
    if "notepad" in app_name:
        subprocess.Popen("notepad.exe")
    elif "word" in app_name:
        word_path = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"  # Adjust path if necessary
        subprocess.Popen(word_path)
    elif "excel" in app_name:
        excel_path = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"  # Adjust path if necessary
        subprocess.Popen(excel_path)
    elif "powerpoint" in app_name:
        ppt_path = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"  # Adjust path if necessary
        subprocess.Popen(ppt_path)
    elif "vs code" in app_name or "visual studio code" in app_name:
        subprocess.Popen(r"C:\Users\ringt\AppData\Local\Programs\Microsoft VS Code\Code.exe")  # Adjust path to your VS Code installation
    else:
        print(f"Application '{app_name}' is not recognized.")

# Function to close applications based on voice commands
def close_application(app_name):
    if "vs code" in app_name or "visual studio code" in app_name:
        os.system("taskkill /f /im Code.exe")
    else:
        print(f"Close functionality for '{app_name}' is not available yet.")

# Function to minimize applications based on voice commands
def minimize_application(app_name):
    try:
        if "vs code" in app_name or "visual studio code" in app_name:
            window = gw.getWindowsWithTitle("Visual Studio Code")[0]
        else:
            window = gw.getWindowsWithTitle(app_name)[0]

        if window:
            window.minimize()
            print(f"Minimized {app_name}")
        else:
            print(f"Could not find an open window for {app_name}")

    except Exception as e:
        print(f"An error occurred while minimizing {app_name}: {e}")
