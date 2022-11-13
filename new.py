from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains 
import time 
import pytesseract as tess 
from PIL import Image
# name=input("Enter Your name:")
# fathername=input("Enter father name:") 
# gender=input("Enter Gender:") 
# age=input("Enter Age:") 
# age='number:'+age 
# yeaar=input("Enter the year:") 
# yeaar='number:'+yeaar 
# montth=input("Enter the month:")
# montth='0'+montth
# datte=input("Enter the date:")
# datte='number:'+datte 
# statte=input("Enter State:")
# districtt=input("Enter District:") 

browser = webdriver.Firefox()
browser.get('https://electoralsearch.in/#!#resultArea') 
button = browser.find_element("xpath",'//*[@id="continue"]').click()

login = browser.find_element("xpath",'//*[@id="name1"]') 
login.send_keys("Poornesh Prahalathan")
flogin = browser.find_element("xpath",'//*[@id="txtFName"]') 
flogin.send_keys("Prahalathan Ramaraj")  
gen = Select(browser.find_element("xpath",'//*[@id="listGender"]')) 
gen.select_by_value('M') 
agenum = Select(browser.find_element("xpath",'//*[@id="ageList"]')) 
agenum.select_by_value('number:19')  
radioclick= browser.find_element("xpath",'//*[@id="radDob"]').click()
year = Select(browser.find_element("xpath",'//*[@id="yearList"]')) 
year.select_by_value('number:2003')
month = Select(browser.find_element("xpath",'//*[@id="monthList"]')) 
month.select_by_value('06') 
date = Select(browser.find_element("xpath",'//*[@id="dayList"]')) 
date.select_by_value('number:9')
state = Select(browser.find_element("xpath",'//*[@id="nameStateList"]')) 
state.select_by_visible_text('Tamil Nadu')  
# district = Select(browser.find_element("xpath",'//*[@id="namelocationList"]')) 
# district.select_by_visible_text(districtt) 

element = browser.find_element("xpath",'//*[@id="captchaDetailImg"]')
element.screenshot('cap.png')

# tess.pytesseract.tesseract_cmd=r'C:\Users\Lenovo\AppData\Local\Tesseract-OCR\tesseract.exe' 
# img = Image.open("cap.png")
# text=tess.image_to_string(img) 

typepanu=input()
capu = browser.find_element("xpath",'//*[@id="txtCaptcha"] ')  
capu.send_keys(typepanu)  
time.sleep(5)

button1 = browser.find_element("xpath",'/html/body/div[4]/div[2]/div/div/div[1]/form/fieldset/div/div[4]/div[2]/div[2]/button').click() 
browser.execute_script("window.scrollTo(0, 200)") 


button3 = browser.find_element("xpath",'/html/body/div[5]/div[3]/div[2]/div/table/tbody/tr/td[1]/form/input[25]').click() 
