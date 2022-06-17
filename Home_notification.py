# pip install selenium --> This will install selenium library
# pip3 install webdriver_manager --> This will install chrome driver in the runtime

import notification as notification
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service #This will import the selenium service in the automation
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#Login
def open_url():
    s = Service(ChromeDriverManager().install()) # This will install driver automatically on the runtime and save it in the cache
    driver = webdriver.Chrome(service = s)
    #driver.maximize.window()
    print(driver.title) #It will print the title in the console
    driver.get('http://imsnepal.com:8080/test/User/Login?ReturnUrl=%2ftest%2f')  # To open the website

    username = driver.find_element(By.XPATH, '//input[@id="UNAME"]')
    username.send_keys("Puja")
    time.sleep(2)  # To open the website upto certain interval
    #driver.quit()  # To quit the driver

    password = driver.find_element(By.XPATH, '//input[@id="Password"]')
    password.send_keys("puja123")
    time.sleep(2)
    #driver.quit()

    login = driver.find_element(By.XPATH, '//input[@type="submit"]')
    login.click() #click() --> call click action
    time.sleep(2)
    #driver.quit()

#Notification_Message module
    notification_message = driver.find_element(By.XPATH, '//input[@id="Message"]')
    notification_message.send_keys("Hello Yudip G, How are you")
    time.sleep(2)

if __name__ == '__main__':
    open_url()