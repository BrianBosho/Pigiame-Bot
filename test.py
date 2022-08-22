from selenium import webdriver
from login import Login
from create_ad import CreateAd
from create_ad import CreateAd
from selenium.webdriver.common.keys import Keys
from manage_ads import ManageAds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import os

chrome_driver_path = "C:\\Users\\Blade\\Desktop\\Selenium\\chromedriver"

silver = {
    "mobile_no": "0706097274",
    "password": "silver@123"

}

ken = {
    "mobile_no": "0772349167",
    "password": "annexy123"

}

# Post assets

driver = webdriver.Chrome(executable_path=chrome_driver_path)

login = Login(driver, ken)
login.login()
login.post_ad()

manage = ManageAds(driver, Keys, EC, WebDriverWait)
manage.open_manage_ads_page()


def delete_drafts():
    manage.open_drafts()
    manage.action_dropdown()
    manage.delete_action()


x = 0

while x < 200:
    delete_drafts()
    x += 1
