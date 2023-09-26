# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import requests
import pwinput # Library for securely entering passwords
from bs4 import BeautifulSoup


# Function to send inspirational quotes
def inspire(number,interval):
    # Send a GET request to the quotes website and parse the HTML content
    site = requests.get('https://quotes.toscrape.com/')
    soup = BeautifulSoup(site.text, 'html.parser')
    
    # Extract quotes and authors from the HTML content
    result = soup.find_all("span",{"class":"text"})
    author = soup.find_all("small",{"class":"author"})
    
    i=0

    # Loop through the quotes and send them
    for a, b in zip(result, author):    
        # Wait for the message input field to be visible
        message = WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Message']")))
        # Send the quote and author's name
        message.send_keys(a.text,b.text,Keys.RETURN)
        i=i+1
        if i == int(number):
            break
        # Wait for the specified interval
        time.sleep(int(interval))            

# Function to log in to Facebook
def login(uname,pwd):
    browser.get('https://www.facebook.com/')
    username = browser.find_element(By.ID, "email")
    username.send_keys(uname)
    password = browser.find_element(By.ID, "pass")
    password.send_keys(pwd)
    submit   = browser.find_element(By.NAME, "login")
    submit.click()

# Function to send messages on Facebook
def sender(name):
    newmessage = WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='New message']")))
    newmessage.click()
    search= WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Send message to']")))
    search.send_keys(name)
    reciever = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[role = 'presentation']")))
    reciever.send_keys(Keys.RETURN)

# Get user inputs for Facebook login, recipient, and quote sending
uname = input("Enter the username: ")
pwd = pwinput.pwinput("Password: ")  # Securely enter the password
number = input("Enter the number of quotes to send : ")
interval = input("Enter the time gap(in seconds) between quotes: ")
name = input("Enter the recipient facebook id : ")

# Configure Chrome WebDriver options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--disable-notifications')
browser = webdriver.Chrome(options=options)

# Log in to Facebook, send messages, and send quotes
login(uname,pwd)
sender(name)
inspire(number,interval)






    





