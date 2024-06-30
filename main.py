import os
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

GOOGLE_FORM_URL = os.getenv("GOOGLE_FORM_URL")
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

# ---------------------------Web Scraping Section--------------------------------

# Get response and contents of the site
response = requests.get(ZILLOW_CLONE_URL)
content = response.content

# Parse the contents of the site
soup = BeautifulSoup(content, 'html.parser')
rentals = soup.select(".StyledPropertyCardDataWrapper")

# Iterate over rentals to get links, prices, and addresses
links = []
prices = []
addresses = []

for rental in rentals:
    # Get links
    href = rental.select_one("a").get("href")
    links.append(href)

    # Get prices
    price_text = rental.select_one("span").text
    if "+" in price_text:
        cleaned_price = price_text.split("+")
        prices.append(cleaned_price[0])
    else:
        cleaned_price = price_text.split("/")
        prices.append(cleaned_price[0])

    # Get addresses
    address_text = rental.select_one("address").text
    semi_cleaned_address_text = address_text.strip().replace("|", "")
    cleaned_address = " ".join(semi_cleaned_address_text.split())
    addresses.append(cleaned_address)

# Create a dictionary to aggregate each rentals' data together into a single key
rentals_dict = {i: (address, price, link) for i, (address, price, link) in enumerate(zip(addresses, prices, links))}

# -----------------------------Data Entry Automation Section------------------------------

# Keep the Chrome browser open after script executes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open the Google form
driver = webdriver.Chrome(chrome_options)
driver.get(GOOGLE_FORM_URL)
time.sleep(2)

# Set all the necessary XPATHs for each element needed
address_xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input"
price_xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input"
link_xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input"
submit_button_xpath = "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div"
next_response_xpath = "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"

# Iterate over the rentals dictionary to send each value to its corresponding element
for key, value in rentals_dict.items():
    address_input = driver.find_element(By.XPATH, address_xpath)
    address_input.send_keys(value[0])

    price_input = driver.find_element(By.XPATH, price_xpath)
    price_input.send_keys(value[1])

    link_input = driver.find_element(By.XPATH, link_xpath)
    link_input.send_keys(value[2])

    submit_button = driver.find_element(By.XPATH, submit_button_xpath)
    submit_button.click()
    time.sleep(2)

    next_response_button = driver.find_element(By.XPATH, next_response_xpath)
    next_response_button.click()
    time.sleep(2)
