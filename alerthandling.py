import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver_path1 = "drivers/chromedriver.exe"
chrome_service = Service(driver_path1)
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")

simpleNav = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a")
simpleNav.click()
Button1 = driver.find_element(By.XPATH,"//*[@id=\"OKTab\"]/button")
Button1.click()
time.sleep(5)
alert = driver.switch_to.alert
alert.accept()

confirmNav = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a")
confirmNav.click()
Button2=driver.find_element(By.XPATH,"//*[@id=\"CancelTab\"]/button")
Button2.click()
time.sleep(5)
alert.dismiss()

txtBoxNav = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a")
txtBoxNav.click()
Button3=driver.find_element(By.XPATH,"//*[@id=\"Textbox\"]/button")
Button3.click()
time.sleep(5)
alert.send_keys("qaclass")
alert.accept()



