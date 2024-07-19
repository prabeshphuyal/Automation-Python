import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time


class TestLogin(unittest.TestCase):
    def setUp(self):
        driver_path = "drivers/chromedriver.exe"
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/index.html")

    def test_login(self):
        driver = self.driver
        try:
            nav_login = driver.find_element(By.ID, "login2")
            nav_login.click()
            time.sleep(5)

            txt_box_username = driver.find_element(By.ID, "loginusername")
            txt_box_username.send_keys("testmorning")

            txt_box_password = driver.find_element(By.ID, "loginpassword")
            txt_box_password.send_keys("test123")

            login_button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
            login_button.click()
            time.sleep(5)

            expected_result = "Welcome testmorning"
            actual_result = driver.find_element(By.ID, "nameofuser").text
            self.assertEqual(actual_result, expected_result, "This is not the same user.")

        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
