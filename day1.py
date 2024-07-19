from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

choice = int(input("Enter 1 for chrome, 2 for firefox, 3 for edge : "))
while True:
    if choice==1:
        driver_path1 = "drivers/chromedriver.exe"
        chrome_service = Service(driver_path1)
        driver = webdriver.Chrome(service=chrome_service)
        driver.maximize_window()
        driver.get("https://bishalkarki.xyz/")
        break

    elif choice==2:
        driver_path2 = "drivers/geckodriver.exe"
        ff_service = Service(driver_path2)
        driver = webdriver.Firefox(service=ff_service)
        driver.maximize_window()
        driver.get("https://bishalkarki.xyz/")
        break

    elif choice==3:
        driver_path3 = "drivers/msedgedriver.exe"
        edge_service = Service(driver_path3)
        driver = webdriver.Edge(service=edge_service)
        driver.maximize_window()
        driver.get("https://bishalkarki.xyz/")
        break
    else:
        print("Invalid input!! Please enter 1,2 or 3")
        break









