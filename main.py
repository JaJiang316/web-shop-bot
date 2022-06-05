import re
from time import sleep
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.maximize_window()
headers = {
    "User-agent": 'My user Agent', }
# URL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
URL = "https://www.bestbuy.com/site/xfx-speedster-swft210-amd-radeon-rx-6600-core-8gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6495949.p?skuId=6495949"
browser.get(URL)
# URL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
# browser.get(URL)


def on_sale():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all("button", class_="add-to-cart-button")[0]
    if(result.text == 'Add to Cart'):
        return True
    else:
        return False


def main():
    # URL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
    # URL = "https://www.bestbuy.com/site/xfx-speedster-swft210-amd-radeon-rx-6600-core-8gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6495949.p?skuId=6495949"
    # browser.get(URL)
    # page = requests.get(URL, headers=headers)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # result = soup.find_all("button", class_="add-to-cart-button")[0]
    browser.find_element(by=By.CLASS_NAME, value="account-button").click()
    time.sleep(2)
    browser.find_element(
        by=By.CLASS_NAME, value='sign-in-btn').click()
    browser.find_element(
        by=By.NAME, value='fld-e').send_keys(os.environ.get('email'))
    browser.find_element(
        by=By.NAME, value='fld-p1').send_keys(os.environ.get('password'))
    browser.find_element(
        by=By.CLASS_NAME, value='cia-form__controls__submit').click()
    if(on_sale() == True):
        time.sleep(4)
        # add item to cart
        browser.find_element(
            by=By.CLASS_NAME, value='add-to-cart-button').click()
        time.sleep(4)
        # go to cart
        browser.find_element(
            by=By.CLASS_NAME, value="go-to-cart-button").click()
        time.sleep(5)
        # select delivery method
        browser.find_element(
            by=By.XPATH, value='//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[3]/fieldset/div[2]/div[1]/div/div/label').click()
        time.sleep(5)
        # click checkout
        browser.find_element(
            by=By.XPATH, value='//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button').click()
        time.sleep(6)
        # continue to payment
        browser.find_element(
            by=By.XPATH, value='//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/section/div[2]/section/div/div/button').click()
        # browser.find_element(
        #     by=By.NAME, value='firstName').send_keys('jason')
        # browser.find_element(
        #     by=By.XPATH, value='//*[@id="lastName"]').send_keys('jiang')
        # browser.find_element(
        #     by=By.XPATH, value='//*[@id="street"]').send_keys('4247 156th St')
        # browser.find_element(
        #     by=By.XPATH, value='//*[@id="city"]').send_keys('flushing')
        # browser.find_element(
        #     by=By.XPATH, value='//*[@id="state"]').send_keys('NY')
        # browser.find_element(
        #     by=By.XPATH, value='//*[@id="zipcode"]').send_keys('11355')


main()
