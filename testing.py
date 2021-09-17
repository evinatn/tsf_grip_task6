from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import requests
import time
from selenium.webdriver.support.select import Select

count=0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.thesparksfoundationsingapore.org/")
print("\n THE SPARKS FOUNDATION")
print(" Task 6: Testing(Automated)")
print(" This program will test the Website Features automatically using Selenium Library.")
print("\n Website for Testing: "+ driver.current_url)
print("\n We are going to test 10+ features of this website")
print("\n\n              CASES FOR TESTING              ")

#Case 1: Verification of Title
print("\n Case 1: Title Verification...")
if(driver.title):
    print(" Verification of Title successful! ")
    print(" Title: "+driver.title)
    count+=1
    
else:
    print(" Title Verification Failed!")

print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

#Case 2: To find and verify the logo of the webpage
print("\n Case 2: Finding and Verification of Logo...")
try:
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*').click()
    print("Logo found and verified successfully!")
    time.sleep(4)
    count+=1
    
except NoSuchElementException:
    print(" No Logo is present! Verification Failed!")

print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

#Case 3: Verification of Navigation Bar
print("\n Case 3: Navigation Bar Verfication...")
try:
    driver.find_element_by_class_name("navbar")
    print(" Verification of Navigation Bar Successfully Completed!")
    time.sleep(2)
    count+=1
    
except NoSuchElementException:
    print(" Navigation Bar Verification Failed!")

print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

#Case 4: Verification of About Us WebPage
print("\n Case 4: About Us WebPage Verification...")
try:
    driver.find_element_by_link_text("About Us").click()
    time.sleep(4)
    driver.find_element_by_link_text("Corporate Partners").click()
    time.sleep(4)
    print(" About Us WebPage visited and verified successfully!")
    count+=1
    
except NoSuchElementException:
    print(" About Us WebPage Verification Failed! No such webpage exists!")

print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")
#Case 5: Verification of HomePage
print("\n Case 5: HomePage Verification...")
try:
    driver.find_element_by_partial_link_text("The Sparks Foundation").click()
    time.sleep(4)
    print("  Verification of HomePage Successfully Completed!")
    count+=1
    
except NoSuchElementException:
    print(" Homepage Verification Failed! HomePage Link doesn't work.")

print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

#Case 6: Verification of Policies and Code WebPage
print("\n Case 6: Policies and Code WebPage Verification...")
try:
    driver.find_element_by_link_text("Policies and Code").click()
    time.sleep(4)
    driver.find_element_by_link_text("Policies").click()
    time.sleep(4)
    driver.find_element_by_link_text("Code of Ethics and Conduct").click()
    time.sleep(4)
    print("  Verification of Policies and Code WebPage Successfully Completed!")
    count+=1
    
except NoSuchElementException:
    print(" Policies and Code WebPage Verification Failed! No such webpage exists!")
    
print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

#Case 7: Verification of Programs WebPage
print("\n Case 7: Programs WebPage Verification...");
try:
    driver.find_element_by_link_text("Programs").click()
    time.sleep(2)
    driver.find_element_by_link_text("Student Scholarship Program").click()
    time.sleep(4)
    driver.find_element_by_link_text("Student Mentorship Program").click()
    time.sleep(4)
    driver.find_element_by_link_text("Student SOS Program").click()
    time.sleep(4)
    driver.find_element_by_link_text("Workshops").click()
    time.sleep(4)
    print("  Verification of Programs WebPage Successfully Completed!")
    count+=1
    
except NoSuchElementException:
    print(" Programs WebPage Verification Failed! No such webpage exists!")

print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

#Case 8: Verification of LINKS Webpage
print("\n Case 8: Links WebPage Verification")
try:
    driver.find_element_by_link_text("LINKS").click()
    time.sleep(2)
    driver.find_element_by_link_text("Software & App").click()
    time.sleep(4)
    driver.find_element_by_link_text("AI in Education").click()
    time.sleep(4)
    print("  Verification of Links WebPage Successfully Completed!")
    count+=1
    
except NoSuchElementException:
    print(" Links Webpage Verification Failed! No such webpage exists!")

print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

#Case 9: Verification of Contact Us WebPage
print("\n Case 9: Contact Us WebPage Verification")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(2)
    contact = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div[2]/p[2]")
    time.sleep(4)

    ##Verification of Contact Details
    if contact.text == "+65-8402-8590, info@thesparksfoundation.sg":
        print(" Contact Information is Correct!")
    else:
        print(" Contact Information is Incorrect!")
    print("  Verification of Contact Us WebPage Successfully Completed!")
    count+=1
    
except NoSuchElementException:
    print(" Contact Us WebPage Verification Failed!")

print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

#Case 10: Verification of Join Us WebPage and Checking the Form Execution:
print("\n Case 10: Join Us Page Verification")
try:
    driver.find_element_by_link_text("Join Us").click()
    time.sleep(2)
    driver.find_element_by_link_text("Why Join Us").click()
    time.sleep(4)
    driver.find_element_by_name("Name").send_keys("Evina Novi Thekkudan")
    time.sleep(4)
    driver.find_element_by_name("Email").send_keys("tn.evina3@gmail.com")
    time.sleep(4)
    select=Select(driver.find_element_by_class_name("form-control"))
    time.sleep(4)
    select.select_by_visible_text("Intern")
    time.sleep(4)
    driver.find_element_by_class_name("button-w3layouts").click()
    time.sleep(4)
    print(" Join Us WebPage Verification Successfully Completed!")
    count+=1
    
except NoSuchElementException:
    print(" Join Us WebPage Verification Failed!")

print("\n 。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

driver.close()

if(count==10):
    print("The Website has been successfully verified and all its features are working as expected!")
    
else:
    print("The website has some features that do not work or are not available!")
