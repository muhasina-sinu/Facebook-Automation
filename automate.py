from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import requests
from bs4 import BeautifulSoup

def inspire():
    site = requests.get('https://quotes.toscrape.com/')
    #print(result.status_code)
    #check the connection to ensure that the website returned content rather than an error.
    #The code returned us a status of 200
    soup = BeautifulSoup(site.text, 'html.parser')
    result = soup.find_all("span",{"class":"text"})
    author = soup.find_all("small",{"class":"author"})
    for a, b in zip(result, author):
        print(a.text)
        print(b.text)

def login():
    browser.get('https://www.facebook.com/')
    username = browser.find_element(By.ID, "email")
    username.send_keys("zarabatulmujeeb@gmail.com")
    password = browser.find_element(By.ID, "pass")
    password.send_keys("Zara_hawwa")
    submit   = browser.find_element(By.NAME, "login")
    submit.click()
    
def sender():
    newmessage = WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='New message']")))
    newmessage.click()
    search= WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Send message to']")))
    search.send_keys("muhasina jalal")
    reciever = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[role = 'presentation']")))
    reciever.send_keys(Keys.RETURN)

    


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--disable-notifications')
browser = webdriver.Chrome(options=options)


login()
sender()

#message = WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Message']")))






    





