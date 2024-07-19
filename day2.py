import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver_path1 = "drivers/chromedriver.exe"
chrome_service = Service(driver_path1)
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()
driver.get("https://demoblaze.com/")

navLogin = driver.find_element(By.ID, "login2")
navLogin.click()
time.sleep(10)
txt_box_username = driver.find_element(By.ID, "loginusername")
txt_box_username.send_keys("testmorning")
txt_box_password = driver.find_element(By.ID, "loginpassword")
txt_box_password.send_keys("test123")

loginButton = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
loginButton.click()
