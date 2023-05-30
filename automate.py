from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import requests
#import getpass
import pwinput
from bs4 import BeautifulSoup

def inspire(number,interval):
    site = requests.get('https://quotes.toscrape.com/')
    #print(result.status_code)
    #check the connection to ensure that the website returned content rather than an error.
    #The code returned us a status of 200
    soup = BeautifulSoup(site.text, 'html.parser')
    result = soup.find_all("span",{"class":"text"})
    author = soup.find_all("small",{"class":"author"})
    
    i=0
    
    for a, b in zip(result, author):    
        message = WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Message']")))
        message.send_keys(a.text,b.text,Keys.RETURN)
        i=i+1
        if i == int(number):
            break
        time.sleep(int(interval))            
                
def login(uname,pwd):
    browser.get('https://www.facebook.com/')
    username = browser.find_element(By.ID, "email")
    username.send_keys(uname)
    password = browser.find_element(By.ID, "pass")
    password.send_keys(pwd)
    submit   = browser.find_element(By.NAME, "login")
    submit.click()
    
def sender(name):
    newmessage = WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='New message']")))
    newmessage.click()
    search= WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Send message to']")))
    search.send_keys(name)
    reciever = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[role = 'presentation']")))
    reciever.send_keys(Keys.RETURN)

 
uname = input("Enter the username: ")
pwd = pwinput.pwinput("Password: ")
number = input("Enter the number of quotes to send : ")
interval = input("Enter the time gap(in seconds) between quotes: ")
name = input("Enter the recipient facebook id : ")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--disable-notifications')
browser = webdriver.Chrome(options=options)

login(uname,pwd)
sender(name)
inspire(number,interval)






    





