# pip install selenium --> This will install selenium library
# pip3 install webdriver_manager --> This will install chrome driver in the runtime

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service #This will import the selenium service in the automation
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Third Approach
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

# Add new Users
    User = driver.find_element(By.LINK_TEXT, 'Users')
    User.click()
    time.sleep(2)

    Add_user = driver.find_element(By.LINK_TEXT, 'Add New User')
    Add_user.click()
    time.sleep(2)

    user_name = driver.find_element(By.XPATH, '//input[@id="UNAME"]')
    user_name.send_keys("DEF")
    time.sleep(1)

    password = driver.find_element(By.XPATH, '//input[@id="Password"]')
    password.send_keys("abc123")
    time.sleep(1)

    Full_name = driver.find_element(By.XPATH, '//input[@id="FULLNAME"]')
    Full_name.send_keys("Ramcharan Yadav")
    time.sleep(1)

    Address = driver.find_element(By.XPATH, '//input[@id="ADDRESS"]')
    Address.send_keys("Putalisadak")
    time.sleep(1)

    Mobile_No = driver.find_element(By.XPATH, '//input[@id="MOBILENO"]')
    Mobile_No.send_keys("9814542883")
    time.sleep(1)

    Replies = driver.find_element(By.XPATH, '//input[@name="REPLY"]')
    Replies.click()
    time.sleep(0.5)

    Promotion = driver.find_element(By.XPATH, '//input[@id="PROMOTIONS"]')
    Promotion.click()
    time.sleep(0.5)

    Advertisement = driver.find_element(By.XPATH, '//input[@id="ADVERTISEMENT"]')
    Advertisement.click()
    time.sleep(0.5)

    users = driver.find_element(By.XPATH, '//input[@id="USERMANAGEMENT"]')
    users.click()
    time.sleep(0.5)

    Order_scheme = driver.find_element(By.XPATH, '//input[@id="ORDERSCHEME"]')
    Order_scheme.click()
    time.sleep(0.5)

    Order = driver.find_element(By.XPATH, '//input[@id="ORDERS"]')
    Order.click()
    time.sleep(0.5)

    Notification = driver.find_element(By.XPATH, '//input[@id="NOTIFICATION"]')
    Notification.click()
    time.sleep(0.5)

    Branch = driver.find_element(By.XPATH, '//input[@id="BRANCH"]')
    Branch.click()
    time.sleep(0.5)

    Category = driver.find_element(By.XPATH, '//input[@id="ITEMCATEGORY"]')
    Category.click()
    time.sleep(0.5)

    Submit = driver.find_element(By.XPATH, '//input[@type="submit"]')
    Submit.click()
    time.sleep(2)


if __name__ == '__main__':
    open_url()