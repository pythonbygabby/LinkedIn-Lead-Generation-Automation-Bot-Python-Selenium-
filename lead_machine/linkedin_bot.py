import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to make it less detectable
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
# Use existing Chrome profile instead of guest profile
# Replace 'Default' with your desired profile name if using a different profile
options.add_argument(r'user-data-dir=C:\Users\Gabriel\AppData\Local\Google\Chrome\User Data')
options.add_argument('profile-directory=Work')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Initialize Chrome driver with webdriver-manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Increase timeouts to handle slow loading
driver.set_page_load_timeout(300)  # 5 minutes
driver.implicitly_wait(10)

driver.get("https://www.linkedin.com/login")

input("Log in manually, then press ENTER...")

print("Enter pressed, continuing with automation...")

# Check if driver is still responsive after manual login
try:
    current_url = driver.current_url
    print(f"Current URL after login: {current_url}")
except Exception as e:
    print(f"Driver not responsive after login: {e}")
    driver.quit()
    exit(1)

profiles = [

    "https://www.linkedin.com/in/example1/",
    "https://www.linkedin.com/in/example2/"
]

for url in profiles:
    try:
        driver.get(url)
    except Exception as e:
        print(f"Error navigating to {url}: {e}")
        break
    time.sleep(random.uniform(5, 8))

    try:
        # Wait for Add button to be clickable with more specific selector
        wait = WebDriverWait(driver, 10)
        Add = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add')]")))
        Add.click()
        print("Add button clicked")
        time.sleep(random.uniform(3, 6))
    except:
        print("No add button")
        # Debug: print available buttons
        try:
            buttons = driver.find_elements(By.TAG_NAME, "button")
            button_texts = [btn.text for btn in buttons if btn.text]
            print(f"Available buttons: {button_texts[:10]}")  # Show first 10
        except:
            print("Could not retrieve buttons")

    time.sleep(random.uniform(15, 30))

driver.quit()
