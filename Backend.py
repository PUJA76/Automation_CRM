# pip install selenium --> This will install selenium library
# pip3 install webdriver_manager --> This will install chrome driver in the runtime

#import Member as Member
import notification as notification
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service #This will import the selenium service in the automation
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Third Approach
def open_url():
    s = Service(ChromeDriverManager().install()) # This will install driver automatically on the runtime and save it in the cache
    driver = webdriver.Chrome(service = s)
    print(driver.title) #It will print the title in the console
    driver.get('http://imsnepal.com:8080/test/User/Login?ReturnUrl=%2ftest%2f')  # To open the website

    username = driver.find_element(By.XPATH, '//input[@id="UNAME"]')
    username.send_keys("yudip")
    time.sleep(2)  # To open the website upto certain interval
    #driver.quit()  # To quit the driver

    password = driver.find_element(By.XPATH, '//input[@id="Password"]')
    password.send_keys("yudip123")
    time.sleep(2)
    #driver.quit()

    login = driver.find_element(By.XPATH, '//input[@type="submit"]')
    login.click() #click() --> call click action
    time.sleep(3)
    #driver.quit()

    notification_message = driver.find_element(By.XPATH, '//input[@id="Message"]')
    notification_message.send_keys("Hello")
    time.sleep(2)

    Message = driver.find_element(By.XPATH, '//a[contains(text(),"Message")]')
    Message.click()
    time.sleep(2)

    Notifications = driver.find_element(By.XPATH, '//a[contains(text(),"Notifications")]')
    Notifications.click()
    time.sleep(2)

    FilterMember = driver.find_element(By.XPATH, '//a[contains(text(),"FilterMember")]')
    FilterMember.click()
    Member_First_name = driver.find_element(By.XPATH, '//input[@id="MemberfName"]')
    Member_First_name.send_keys("Puja")  # send_keys() --> Type something
    time.sleep(2)
    Member_last_name = driver.find_element(By.XPATH, '//input[@id="MemberlName"]')
    Member_last_name.send_keys("Bohara")
    time.sleep(2)
    Street = driver.find_element(By.XPATH, '//input[@id="street"]')
    Street.send_keys("Putalishadak")
    time.sleep(2)
    Mobile_No = driver.find_element(By.XPATH, '//input[@id="MobileNo"]')
    Mobile_No.send_keys("9814542883")
    time.sleep(2)





if __name__ == '__main__':
     open_url()










# Important Note
"""
text() --> pull the text 
select() --> Select from dropdown
"""