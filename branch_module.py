# pip install selenium --> This will install selenium library
# pip3 install webdriver_manager --> This will install chrome driver in the runtime

from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service  # This will import the selenium service in the automation
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Third Approach
# Login

def open_url():
    s = Service(
        ChromeDriverManager().install())  # This will install driver automatically on the runtime and save it in the cache
    driver = webdriver.Chrome(service=s)
    # driver.maximize.window()
    print(driver.title)  # It will print the title in the console
    driver.get('http://imsnepal.com:8080/test/User/Login?ReturnUrl=%2ftest%2f')  # To open the website

    username = driver.find_element(By.XPATH, '//input[@id="UNAME"]')
    username.send_keys("Puja")
    time.sleep(1)  # To open the website upto certain interval
    # driver.quit()  # To quit the driver

    password = driver.find_element(By.XPATH, '//input[@id="Password"]')
    password.send_keys("puja123")
    time.sleep(1)
    # driver.quit()

    login = driver.find_element(By.XPATH, '//input[@type="submit"]')
    login.click()  # click() --> call click action
    time.sleep(1)
    # driver.quit()

    # Branch module --> Add,Edit or Delete Branch
    Branch = driver.find_element(By.LINK_TEXT, 'Branch')
    Branch.click()
    time.sleep(1)

    # After Entering the Branch, Add a new Branch
    Add_New_Branch = driver.find_element(By.LINK_TEXT, 'Add New Branch')
    Add_New_Branch.click()
    time.sleep(1)

# Ignore Longitude and Latitude
    '''
    # Now enter values in the fields
    Longitude = driver.find_element(By.XPATH, '//input[id="lon"]')
    Longitude.send_keys("85.32305461277303")
    time.sleep(1)

    Latitude = driver.find_element(By.XPATH, '//input[id="lat"]')
    Latitude.send_keys("27.714639384386423")
    time.sleep(1)
'''

    Branch_Name = driver.find_element(By.XPATH, '//input[@id="NAME"]')
    Branch_Name.send_keys("Kathmandu Branch")
    time.sleep(1)

    Address = driver.find_element(By.XPATH, '//input[@id="ADDRESS"]')
    Address.send_keys("Kathmandu")
    time.sleep(1)

    Contact = driver.find_element(By.XPATH, '//input[@id="CONTACT_NO"]')
    Contact.send_keys("9814542883")
    time.sleep(1)

    Initial = driver.find_element(By.XPATH, '//input[@id="INITIAL"]')
    Initial.send_keys("Test")
    time.sleep(1)

    Store_Manager = driver.find_element(By.XPATH, '//input[@name="STOREMANAGER"]')
    Store_Manager.send_keys("Mr. Ram keshwor Parshad")
    time.sleep(1)

    Email = driver.find_element(By.XPATH, '//input[@id="STOREMANAGEREMAIL"]')
    Email.send_keys("ramparshad875@gmail.com")
    time.sleep(1)

    image_url = driver.find_element(By.XPATH, '//input[@id="IMAGEURL"]')
    image_url.send_keys("https://en.wikipedia.org/wiki/Common_sunflower")
    time.sleep(1)

    submit = driver.find_element(By.XPATH, '//input[@type="submit"]')
    submit.click()
    time.sleep(2)

if __name__ == '__main__':
    open_url()
