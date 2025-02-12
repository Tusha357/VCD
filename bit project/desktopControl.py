import os
import pyautogui
from ctypes import windll

def change_brightness(change):
    try:
        windll.user32.SendMessageW(0xFFFF, 0x009A, 0, int(change))
        print(f"Brightness changed by {change} units.")
    except Exception as e:
        print(f"Error changing brightness: {e}")

def change_volume(change):
    try:
        pyautogui.press("volumeup" if change > 0 else "volumedown")
        print(f"Volume changed by {abs(change)} units.")
    except Exception as e:
        print(f"Error changing volume: {e}")

def toggle_wifi(enable):
    try:
        if enable:
            pyautogui.hotkey("win", "a")
            pyautogui.click(x=100, y=100)  # Update x, y to click the Wi-Fi button
        else:
            pyautogui.hotkey("win", "a")
            pyautogui.click(x=100, y=200)  # Update x, y to click the Wi-Fi button to disable
        print(f"Wi-Fi {'enabled' if enable else 'disabled'}.")
    except Exception as e:
        print(f"Error toggling Wi-Fi: {e}")

def toggle_night_light(enable):
    try:
        pyautogui.hotkey("win", "a")
        if enable:
            pyautogui.click(x=100, y=300)  # Update x, y to click the Night Light button
        else:
            pyautogui.click(x=100, y=400)  # Update x, y to click the Night Light button to disable
        print(f"Night Light {'enabled' if enable else 'disabled'}.")
    except Exception as e:
        print(f"Error toggling Night Light: {e}")

def toggle_airplane_mode(enable):
    try:
        pyautogui.hotkey("win", "a")
        if enable:
            pyautogui.click(x=100, y=500)  # Update x, y to click the Airplane Mode button
        else:
            pyautogui.click(x=100, y=600)  # Update x, y to click the Airplane Mode button to disable
        print(f"Airplane Mode {'enabled' if enable else 'disabled'}.")
    except Exception as e:
        print(f"Error toggling Airplane Mode: {e}")

def shutdown_pc():
    try:
        os.system("shutdown /s /t 1")
        print("Shutting down the PC.")
    except Exception as e:
        print(f"Error shutting down PC: {e}")