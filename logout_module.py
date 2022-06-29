from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service #This will import the selenium service in the automation
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def open_url():
    s = Service(ChromeDriverManager().install()) # This will install driver automatically on the runtime and save it in the cache
    driver = webdriver.Chrome(service = s)
    #driver.maximize.window()
    print(driver.title) #It will print the title in the console
    driver.get('http://imsnepal.com:8080/test/User/Login?ReturnUrl=%2ftest%2f')  # To open the website

    username = driver.find_element(By.XPATH, '//input[@id="UNAME"]')
    username.send_keys("Puja")
    time.sleep(1)  # To open the website upto certain interval
    #driver.quit()  # To quit the driver

    password = driver.find_element(By.XPATH, '//input[@id="Password"]')
    password.send_keys("puja123")
    time.sleep(1)
    #driver.quit()

    login = driver.find_element(By.XPATH, '//input[@type="submit"]')
    login.click() #click() --> call click action
    time.sleep(2)
    #driver.quit()

#LogOut

