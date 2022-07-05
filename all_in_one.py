# pip install selenium --> This will install selenium library
# pip3 install webdriver_manager --> This will install chrome driver in the runtime

#import Member as Member
import by as by
import notification as notification
#import numbers list
#import random

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

#Notification_Message module
    notification_message = driver.find_element(By.XPATH, '//input[@id="Message"]')
    notification_message.send_keys("Hello")
    time.sleep(2)

#Message & Reply module
    Message = driver.find_element(By.XPATH, '//a[contains(text(),"Message")]')
    Message.click()
    time.sleep(2)

    Reply = driver.find_element(By.XPATH, '//a[contains(text(),"Reply")]')
    Reply.click()
    Type_reply = driver.find_element(By.XPATH, '//textarea[@id="txtReply"]')
    Type_reply.send_keys("Hello")
    time.sleep(2)

#Notification module
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
    Street.send_keys("Putalishdak")
    time.sleep(2)

    Mobile_No = driver.find_element(By.XPATH, '//input[@id="MobileNo"]')
    Mobile_No.send_keys("9814542883")
    time.sleep(2)

    Member_Birthday = driver.find_element(By.XPATH, '//input[@id="dtBFrom"]')
    Member_Birthday.send_keys("12/08/2008") #mm/dd/yy
    time.sleep(2)

    Wedding_Aniversary = driver.find_element(By.XPATH, '//input[@id="dtWFrom"]')
    Wedding_Aniversary.send_keys("05/25/2021")
    time.sleep(2)

    Submit = driver.find_element(By.XPATH, '//input[@type="submit"]')
    Submit.click()  # click() --> call click action
    time.sleep(3)

#After the Member Profile Enter the Common Message .
    Common_Message = driver.find_element(By.XPATH, '//input[@id="CommonMessage"]')
    Common_Message.send_keys("New users")
    time.sleep(2)

    Submit = driver.find_element(By.XPATH, '//input[@type="submit"]')
    Submit.click()  # click() --> call click action
    time.sleep(3)

#FeedBacks Module
    Feedbacks = driver.find_element(By.LINK_TEXT, 'Feedbacks')
    Feedbacks.click()
    time.sleep(3)

    # Category Module
    Category = driver.find_element(By.LINK_TEXT, 'Category')
    Category.click()
    time.sleep(2)

#Add New Category(Click)
    Add_New_Category = driver.find_element(By.XPATH, '//a[normalize-space()="Add New Category"]')
    Add_New_Category.click()
    time.sleep(2)

    Add = driver.find_element(By.XPATH, '//input[@id="CNAME"]')
    Add.send_keys("Demo Category1")
    time.sleep(2)

#Submit the new category name.
    Submit = driver.find_element(By.XPATH, '//input[@type="submit"]')
    Submit.click()
    time.sleep(2)

    # Edit the existing Category.
    Edit_Category = driver.find_element(By.XPATH, '(//a[contains(text(),"Edit")])[2]')
    Edit_Category.click()
    time.sleep(2)
    category = driver.find_element(By.XPATH, '//input[@id="CNAME"]')
    category.clear()
    time.sleep(2)

# Remove the old data and enter new one.
    Edit_Category = driver.find_element(By.XPATH, '//input[@id="CNAME"]')
    Edit_Category.clear()
    Edit_Category.send_keys("Ladies shoes")
    time.sleep(2)


#Product Promotion
    Promotion = driver.find_element(By.XPATH, '//a[normalize-space()="Promotions"]') #(By.XPATH, '//a[contain(text),"Promotions")]')
    Promotion.click()
    time.sleep(2)

    Add_New_Promotion = driver.find_element(By.XPATH, '//a[normalize-space()="Add New Promotion"]')
    Add_New_Promotion.click()
    time.sleep(2)

#After clicking Add new product and goes to new page with this kind of form.
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
    Category.send_keys("test dfa")
    time.sleep(2)

    image_url = driver.find_element(By.XPATH, '//input[@id="IMAGEURL"]')
    image_url.send_keys("http://imsnepal.com:8080/ImsPosMem/upload_images/TEST/PROMOTIONSIMAGE/201924-test.jfif")
    time.sleep(2)

    Discount_Percent = driver.find_element(By.XPATH, '//input[@id="DiscountPercent"]')
    Discount_Percent.clear()
    Discount_Percent.send_keys("10%")
    time.sleep(2)

#New_Product_old_Price
    old_price = driver.find_element(By.XPATH, '//input[@id="OldPrice"]')
    old_price.clear()
    old_price.send_keys("500")
    time.sleep(2)

#Product New Price
    New_price = driver.find_element(By.XPATH, '//input[@id="NewPrice"]')
    New_price.clear()
    New_price.send_keys("700")
    time.sleep(2)

# Submit the new category name.
    Submit = driver.find_element(By.XPATH, '//input[@type="submit"]')
    Submit.click()
    time.sleep(2)
    """
#Advertisement Module
    Advertisement = driver.find_element(By.LINK_TEXT, 'Advertisement')
    Advertisement.click()
    time.sleep(2)  """


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

# Add new Users
    User = driver.find_element(By.LINK_TEXT, 'Users')
    User.click()
    time.sleep(2)

    Add_user = driver.find_element(By.LINK_TEXT, 'Add New User')
    Add_user.click()
    time.sleep(2)

    user_name = driver.find_element(By.XPATH, '//input[@id="UNAME"]')
    user_name.send_keys("Deepak")
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


""" text() --> pull the text 
select() --> Select from dropdown
"""