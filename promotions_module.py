
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

#Product Promotion
    Promotion = driver.find_element(By.XPATH, '//a[normalize-space()="Promotions"]') #(By.XPATH, '//a[contain(text),"Promotions")]')
    Promotion.click()
    time.sleep(2)

    Add_New_Promotion = driver.find_element(By.XPATH, '//a[normalize-space()="Add New Promotion"]')
    Add_New_Promotion.click()
    time.sleep(2)

    # After clicking Add new product and goes to new page with this kind of form.
    Product_Id = driver.find_element(By.XPATH, '//input[@id="PRODUCTID"]')
    Product_Id.send_keys("001")
    time.sleep(2)

    Description = driver.find_element(By.XPATH, '//textarea[@id="DESCRIPTION"]')
    Description.send_keys("This is test product")
    time.sleep(2)

    Begin_Date = driver.find_element(By.XPATH, '//input[@id="dtBegin"]')
    Begin_Date.send_keys("06/15/2022")
    time.sleep(2)

    End_Date = driver.find_element(By.XPATH, '//input[@id="dtEnd"]')
    End_Date.send_keys("12/28/2022")
    time.sleep(2)

    Message = driver.find_element(By.XPATH, '//textarea[@id="MESSAGE"]')
    Message.send_keys("Hello World")
    time.sleep(2)

    Category = driver.find_element(By.XPATH, '//select[@id="CATEGORYID"]')
    Category.click()
    time.sleep(1)


    # number_list = [3]

    image_url = driver.find_element(By.XPATH, '//input[@id="IMAGEURL"]')
    image_url.send_keys("http://imsnepal.com:8080/ImsPosMem/upload_images/TEST/PROMOTIONSIMAGE/201924-test.jfif")
    time.sleep(2)

    Discount_Percent = driver.find_element(By.XPATH, '//input[@id="DiscountPercent"]')
    Discount_Percent.clear()
    Discount_Percent.send_keys("10%")
    time.sleep(2)

    # New_Product_old_Price
    old_price = driver.find_element(By.XPATH, '//input[@id="OldPrice"]')
    old_price.clear()
    old_price.send_keys("500")
    time.sleep(2)

    # Product New Price
    New_price = driver.find_element(By.XPATH, '//input[@id="NewPrice"]')
    New_price.clear()
    New_price.send_keys("700")
    time.sleep(2)

    # Submit the new category name.
    Submit = driver.find_element(By.XPATH, '//input[@type="submit"]')
    Submit.click()
    time.sleep(2)

if __name__ == '__main__':
    open_url()
