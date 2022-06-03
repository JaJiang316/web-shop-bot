import re
from time import sleep
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()


def main():
    headers = {
        "User-agent": 'My user Agent', }
    # URL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
    URL = "https://www.bestbuy.com/site/xfx-speedster-swft210-amd-radeon-rx-6600-core-8gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6495949.p?skuId=6495949"
    browser.get(URL)
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all("button", class_="add-to-cart-button")[0]
    if(result.text == 'Add to Cart'):
        browser.find_element(
            by=By.CLASS_NAME, value="add-to-cart-button").click()
        sleep(3)
        browser.find_element(
            by=By.CLASS_NAME, value="go-to-cart-button").click()
        sleep(3)
        browser.find_element(
            by=By.XPATH, value='//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[1]/div[4]/ul/li/section/div[2]/div[2]/form/div[3]/fieldset/div[2]/div[1]/div/div/label').click()
        sleep(3)
        browser.find_element(
            by=By.XPATH, value='//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button').click()


main()
