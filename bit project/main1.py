import os
from time import sleep
import warnings
from threading import Thread
import subprocess  # To run external Python scripts
import signal  # To stop the gesture control process


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pywhatkit
from difflib import get_close_matches



# Replace with your desktop control imports
from chromeControll import (
    open_youtube, open_google, open_instagram, open_github, open_linkedin, send_whatsapp_message,
    open_new_tab, close_current_tab, close_specific_tab, go_to_tab, play_video, pause_video, scroll_page
)
from desktopControl import (
    change_brightness, change_volume, toggle_wifi, toggle_night_light, toggle_airplane_mode, shutdown_pc
)

# Ignore unnecessary warnings
warnings.simplefilter("ignore")

# List of valid commands for suggestion purposes
valid_commands = [
    "open youtube", "open google", "open instagram", "send message",
    "open a new tab", "close current tab", "close tab", "go to tab",
    "brightness up", "brightness down", "volume up", "volume down",
    "turn on wifi", "turn off wifi", "turn on night light", "turn off night light",
    "turn on airplane mode", "turn off airplane mode", "pause the video", "play the video", "close all tabs"
]

# Store process reference to control gesture activation/deactivation
gesture_control_active = False
gesture_process = None

# Function to activate hand gesture control
def activate_gesture_control():
    global gesture_control_active, gesture_control_process
    if gesture_control_active:
        print("Hand gesture mouse is already running.")
    else:
        print("Activating hand gesture mouse...")
        gesture_control_active = True
        # Start the hand gesture control (Gesture_control.py) in a separate process
        gesture_control_process = subprocess.Popen(['python', 'Gesture_control.py'])
        print("Hand gesture mouse activated.")

# Function to deactivate hand gesture control
def deactivate_gesture_control():
    global gesture_control_active, gesture_control_process
    if gesture_control_active:
        print("Deactivating hand gesture mouse...")
        gesture_control_process.terminate()  # Stop the process
        gesture_control_active = False
        print("Hand gesture mouse deactivated.")
    else:
        print("Hand gesture mouse is not running.")



# Function to process commands
def process_command(command):
    global gesture_process

# Function to get closest matching command
def suggest_command(command):
    matches = get_close_matches(command, valid_commands, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return None

# Function to process commands
def process_command(command):
    if "open youtube" in command:
        if "and search" in command:
            search_query = command.split("and search")[-1].strip()
            pywhatkit.playonyt(search_query)
        else:
            open_youtube()

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

    elif "open a new tab" in command:
        open_new_tab()

    elif "close current tab" in command:
        close_current_tab()

    elif "close all tabs" in command:
        close_all_tabs()

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
    
    elif "activate hand gesture mouse" in command:
        activate_gesture_control()

    elif "deactivate hand gesture mouse" in command:
        deactivate_gesture_control()

    
# Function to close all tabs
def close_all_tabs():
    driver = webdriver.Chrome()  # Initialize a new driver instance
    driver.get('chrome://tabs/')  # Navigate to the tabs page
    close_buttons = driver.find_elements(By.XPATH, '//div[@role="tab"]//button[@title="Close Tab"]')
    for button in close_buttons:
        button.click()
    driver.quit()
    print("All tabs closed.")

# Function to listen for commands from the text file
def listen_for_command():
    try:
        output_file_path = "SpeechRecognition.txt"
        with open(output_file_path, "r") as file:
            command = file.read().strip().lower()

            if not command:
                return True  # No new command, keep listening

            print(f"You said: {command}")
            
            # Process command or suggest alternatives
            process_command(command)

            # Clear the file after reading to avoid repetition
            with open(output_file_path, "w") as file:
                file.write("")

    except FileNotFoundError:
        print("Voice command file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return True

# Function to start voice detection
def start_voice_detection():
    try:
        print("Wait a second, I am setting up your voice control desktop.")
        
        # Set up Chrome options
        chrome_driver_path = 'chromedriver.exe'
        chrome_options = Options()
        chrome_options.headless = False
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')
        service = Service(chrome_driver_path)
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--use-fake-device-for-media-stream")

        # Initialize the Chrome driver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        url = "https://dictation.io/speech"
        driver.get(url)
        sleep(15)

        # Enable microphone access and start capturing
        driver.execute_script('navigator.mediaDevices.getUserMedia({ audio: true })')
        start_button_xpath = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[1]/a"
        driver.find_element(By.XPATH, value=start_button_xpath).click()
        print("Microphone is turned on")

        # Continuous loop to capture text and write to file
        while True:
            text_element_xpath = '/html/body/div[3]/section/div/div/div[2]/div/div[2]'
            text = driver.find_element(By.XPATH, value=text_element_xpath).text

            if text:
                text = text.strip()

                # Write the text to a file
                output_file_path = "SpeechRecognition.txt"
                with open(output_file_path, "w") as file_write:
                    file_write.write(text)
                print(f"Captured text: {text}")

                # Clear the text for the next capture
                clear_button_xpath = '/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[2]/a[8]'
                driver.find_element(By.XPATH, value=clear_button_xpath).click()

            sleep(2)  # Adjust the sleep time as needed

    except Exception as e:
        print(f"Error occurred: {e}")

# Main function to run both voice detection and command processing
if __name__ == "__main__":
    # Start the voice detection process
    voice_detection_thread = Thread(target=start_voice_detection)
    voice_detection_thread.start()

    # Simultaneously process commands from the text file
    while True:
        if not listen_for_command():
            break
        sleep(2)  # Adjust the sleep time for checking commands
