import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import warnings

# Ignore unnecessary warnings
warnings.simplefilter("ignore")

# Constants
CHROME_DRIVER_PATH = 'chromedriver.exe'
DICTATION_URL = "https://dictation.io/speech"
CLEAR_BUTTON_XPATH = '/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[2]/a[8]'
START_BUTTON_XPATH = "/html/body/div[3]/section/div/div/div[2]/div/div[3]/div[1]/a"
TEXT_ELEMENT_XPATH = '/html/body/div[3]/section/div/div/div[2]/div/div[2]'
OUTPUT_FILE_PATH = "SpeechRecognition.txt"

def setup_driver():
    """Set up the Chrome WebDriver with specified options."""
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    chrome_options.add_argument("--use-fake-device-for-media-stream")
    
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    return driver

def initialize_dictation(driver):
    """Initialize the dictation page and start the microphone."""
    driver.get(DICTATION_URL)

    # Attempt to click an element to ensure the page is fully loaded
    try:
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/div").click()
    except Exception:
        pass

    # Wait for the page to load
    sleep(15)
    
    # Execute JavaScript to enable microphone access
    driver.execute_script('navigator.mediaDevices.getUserMedia({ audio: true })')
    sleep(1)

    # Click the "Clear" button to reset
    driver.find_element(by=By.XPATH, value=CLEAR_BUTTON_XPATH).click()
    sleep(1)

    # Click the start button
    driver.find_element(by=By.XPATH, value=START_BUTTON_XPATH).click()
    print("Microphone is turned on")

def capture_text(driver):
    """Continuously capture and write text to a file."""
    while True:
        try:
            # Get the text from the dictation interface
            text = driver.find_element(by=By.XPATH, value=TEXT_ELEMENT_XPATH).text
            if text:
                # Click the "Clear" button to reset
                driver.find_element(by=By.XPATH, value=CLEAR_BUTTON_XPATH).click()
                text = text.strip()
                
                # Write the text to a file
                with open(OUTPUT_FILE_PATH, "w") as file_write:
                    file_write.write(text)
                print(f"Captured text: {text}")
                
            sleep(2)  # Adjust the sleep time as needed
            
        except Exception as e:
            print(f"Error capturing text: {e}")
            sleep(5)  # Wait before retrying

def main():
    """Main function to set up the driver, initialize dictation, and capture text."""
    try:
        driver = setup_driver()
        initialize_dictation(driver)
        capture_text(driver)
    except Exception as e:
        print("Error: Unable to configure the ChromeDriver properly.")
        print("To resolve this error, make sure to set up the ChromeDriver correctly.")
        print(e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
