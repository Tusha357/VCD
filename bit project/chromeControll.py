import os
import webbrowser
import pyautogui
import pywhatkit
import requests
import pyttsx3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def check_internet():
    try:
        requests.get('https://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        print("It seems like there's no internet connection. Please connect to the internet and try again.")
        return False

def open_new_tab():
    if not check_internet():
        return
    pyautogui.hotkey("ctrl", "t")
    print("Opened a new tab.")

def close_current_tab():
    pyautogui.hotkey("ctrl", "w")
    print("Closed the current tab.")

def close_specific_tab(tab_number):
    pyautogui.hotkey("ctrl", str(tab_number))
    pyautogui.hotkey("ctrl", "w")
    print(f"Closed tab {tab_number}.")

def go_to_tab(tab_number):
    pyautogui.hotkey("ctrl", str(tab_number))
    print(f"Switched to tab {tab_number}.")

def open_youtube():
    if not check_internet():
        return
    webbrowser.open("https://www.youtube.com")
    print("Opened YouTube.")

def open_google(search_query=None):
    if not check_internet():
        return
    if search_query:
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        print(f"Opened Google and searched for '{search_query}'.")
    else:
        webbrowser.open("https://www.google.com")
        print("Opened Google.")

def open_instagram():
    if not check_internet():
        return
    webbrowser.open("https://www.instagram.com")
    print("Opened Instagram.")

def open_github():
    if not check_internet():
        return
    webbrowser.open("https://www.github.com")
    print("Opened GitHub.")

def open_linkedin():
    if not check_internet():
        return
    webbrowser.open("https://www.linkedin.com")
    print("Opened LinkedIn.")

def send_whatsapp_message(person, message):
    if not check_internet():
        return

    phone_numbers = {
        "nayan": "+919404837391",
        "prathamesh": "+918767825068",
        "yogesh": "+918007220126",
        "tushar":"+918766095674"
        # Add more contacts here
    }

    if person in phone_numbers:
        phone_number = phone_numbers[person]
        print(f"Phone number to be used: {phone_number}")  # Debugging
        print(f"Message to be sent: {message}")  # Debugging
        try:
            pywhatkit.sendwhatmsg_instantly(phone_number, message)
            print(f"Sending your message to {person}...")
        except Exception as e:
            print(f"An error occurred while sending the message: {e}")
    else:
        print(f"Sorry, I don't have the phone number for {person}. Please check the contact name or add the number.")

def call_whatsapp_contact(person):
    if not check_internet():
        return

    phone_numbers = {
        "nayan": "+919404837391",
        "prathamesh": "+918767825068",
        "yogesh": "+918007220126",
        "tushar": "+918766095674"
        # Add more contacts here
    }

    if person in phone_numbers:
        phone_number = phone_numbers[person]
        try:
            pywhatkit.sendwhatmsg_instantly(phone_number, " ", 1, True)  # Starts the call
            print(f"Calling {person} via WhatsApp...")
        except Exception as e:
            print(f"An error occurred while calling {person}: {e}")
    else:
        print(f"Sorry, I don't have the phone number for {person}. Please check the contact name or add the number.")

        
def play_video():
    pyautogui.press("playpause")
    print("Played the video.")

def pause_video():
    pyautogui.press("playpause")
    print("Paused the video.")

def scroll_page(direction):
    if direction == 'up':
        pyautogui.scroll(50)
    elif direction == 'down':
        pyautogui.scroll(-50)
    print(f"Scrolled {direction}.")