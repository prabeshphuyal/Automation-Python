from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set up the WebDriver
driver_path = "drivers/chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Maximize the window and open the website
driver.maximize_window()
driver.get("https://demoblaze.com/index.html")


# Find the login elements and perform login
try:
    nav_login = driver.find_element(By.ID, "login2")
    nav_login.click()
    time.sleep(5)  # Wait for the login modal to appear

    # Attempt to find the username and password fields
    try:
        txt_box_username = driver.find_element(By.ID, "loginusernam")
        txt_box_username.send_keys("testmorning")
    except NoSuchElementException:
        txt_box_username = driver.find_element(By.ID, "loginusername")
        txt_box_username.send_keys("testmorning")

    txt_box_password = driver.find_element(By.ID, "loginpassword")
    txt_box_password.send_keys("test123")

    login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_button.click()
except NoSuchElementException as e:
    print(f"Unable to find an element: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser after the operations
    driver.quit()
