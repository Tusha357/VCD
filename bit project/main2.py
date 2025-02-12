import os
import time
import warnings
import pyttsx3
import speech_recognition as sr
from threading import Thread

import subprocess
import pywhatkit
from openapp import open_application

from chromeControll import (
    open_youtube, open_google, open_instagram, open_github, open_linkedin, send_whatsapp_message,
    open_new_tab, close_current_tab, close_specific_tab, go_to_tab, play_video, pause_video, scroll_page, call_whatsapp_contact
)
from desktopControl import (
    change_brightness, change_volume, toggle_wifi, toggle_night_light, toggle_airplane_mode, shutdown_pc
)

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Ignore unnecessary warnings
warnings.simplefilter("ignore")

# Set global flags
gesture_control_active = False
gesture_process = None

# Initialize speech recognition
recognizer = sr.Recognizer()
mic = sr.Microphone()

# Function to speak a text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to activate hand gesture-based mouse control
def activate_gesture_control():
    global gesture_control_active, gesture_process
    if not gesture_control_active:
        gesture_control_active = True
        gesture_process = subprocess.Popen(['python', 'gesture_control.py'])  # Replace with actual gesture control script
        speak("Gesture control activated.")
        print("Gesture control activated")

# Function to deactivate hand gesture-based mouse control
def deactivate_gesture_control():
    global gesture_control_active, gesture_process
    if gesture_control_active and gesture_process:
        gesture_control_active = False
        gesture_process.terminate()
        gesture_process = None
        speak("Gesture control deactivated.")
        print("Gesture control deactivated")

# Function to listen for commands
def listen_for_commands():
    while True:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for commands...")

                # Listen for input
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                print(f"Heard: {command}")

                process_command(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")

# Function to process actual commands
def process_command(command):
    if "open youtube" in command:
        if "and search" in command:
            search_query = command.split("and search")[-1].strip()
            pywhatkit.playonyt(search_query)
        else:
            open_youtube()

    elif "open google" in command:
        if "and search" in command:
            search_query = command.split("and search")[-1].strip()
            open_google(search_query)
        else:
            open_google()

    elif "open instagram" in command:
        open_instagram()

    elif "open github" in command:
        open_github()
    
    elif "open linkedin" in command:
        open_linkedin()

    elif "send message" in command:
        parts = command.split("send message")[-1].strip().split(" to ")
        if len(parts) == 2:
            message, person = parts
            send_whatsapp_message(person.strip(), message.strip())

    elif "call to" in command:
        person = command.split("call to")[-1].strip()
        call_whatsapp_contact(person)

    elif "open a new tab" in command:
        open_new_tab()

    elif "open" in command:
        app_name = command.split("open")[-1].strip()
        open_application(app_name)

    elif "close current tab" in command:
        close_current_tab()

    elif "close" in command and "tab" in command:
        try:
            tab_number = int(command.split("close")[1].split("tab")[0].strip())
            close_specific_tab(tab_number)
        except ValueError:
            print("Sorry, I did not understand the tab number.")

    elif "go to" in command and "tab" in command:
        try:
            tab_number = int(command.split("go to")[1].split("tab")[0].strip())
            go_to_tab(tab_number)
        except ValueError:
            print("Sorry, I did not understand the tab number.")

    elif "brightness up" in command:
        change_brightness(10)

    elif "brightness down" in command:
        change_brightness(-10)

    elif "volume up" in command:
        change_volume(10)

    elif "volume down" in command:
        change_volume(-10)

    elif "turn on wifi" in command:
        toggle_wifi(True)

    elif "turn off wifi" in command:
        toggle_wifi(False)

    elif "turn on night light" in command:
        toggle_night_light(True)

    elif "turn off night light" in command:
        toggle_night_light(False)

    elif "turn on airplane mode" in command:
        toggle_airplane_mode(True)

    elif "turn off airplane mode" in command:
        toggle_airplane_mode(False)

    elif "pause the video" in command:
        pause_video()

    elif "play the video" in command:
        play_video()

    elif "scroll up" in command:
        scroll_page('up')

    elif "scroll down" in command:
        scroll_page('down')

    elif "shut down my pc" in command:
        shutdown_pc()

    elif "activate gesture control" in command:
        activate_gesture_control()

    elif "deactivate gesture control" in command:
        deactivate_gesture_control()

    else:
        print(f"Command not recognized: {command}")

# Main function to run the system
if __name__ == "__main__":
    listen_for_commands()
