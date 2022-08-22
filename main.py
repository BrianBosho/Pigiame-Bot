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

elyne = {
    "mobile_no": "0714689677",
    "password": "31120529"

}

# Post assets

driver = webdriver.Chrome(executable_path=chrome_driver_path)

login = Login(driver, elyne)
login.login()
login.post_ad()

# manage = ManageAds(driver, Keys, EC, WebDriverWait)
# manage.open_manage_ads_page()


# def delete_drafts():
#     manage.open_drafts()
#     manage.action_dropdown()
#     manage.delete_action()
#
#
# def delete_offline():
#     manage.open_offline()
#     manage.action_dropdown()
#     manage.delete_action()
#
#
# def delete_rejected():
#     # implement implicit waits to fix this issue
#     manage.open_rejected()
#     manage.action_dropdown()
#     manage.delete_action()


# i = 0
# while i < 200:
#     delete_rejected()
#     i += 1

# post a new ad

old_titles = []

title_list = []


def get_title():
    title = random.choice(title_list) + " " + random.choice(title_list) + " " + random.choice(
        title_list) + " wall to wall carpets"
    repeat = title in old_titles
    while repeat:
        title = random.choice(title_list) + " " + random.choice(title_list) + " " + random.choice(
            title_list) + " grass carpets"
        repeat = title in old_titles
    return title


description_list = []
images_list = []

# images_path = "C:\\Users\\Blade\\Desktop\\Web Automation\\pillow_editor\\saved_wmk\\"
images_path = "C:\\Users\\Blade\\Desktop\\Web Automation\\pillow_editor\\kenwtw\\"
my_pics = os.listdir(images_path)

title_file = open("wall to wall adjectives.txt", "r")
description_file = open("wall to wall descriptions.txt", "r")
for line in title_file:
    title_list.append(line.strip())

for line in description_file:
    description_list.append(line.strip())

for pic in my_pics:
    full_path = images_path + pic
    images_list.append(full_path)

random.shuffle(description_list)
random.shuffle(images_list)

call_to_action = "Call/Text/Whatsapp to get your items today"


def create_new_post(driver, Keys, title, description, curtain_price, curtain_images, WebDriverWait, EC):
    post = CreateAd(driver, Keys, title, description, curtain_price, curtain_images)
    try:
        post.select_category()
        try:
            post.select_subcategory()
            try:
                post.fill_ad_details()
                try:
                    post.upload_images(curtain_images)
                    try:
                        post.select_product()
                    except Exception as e:
                        print("could not select product", e)
                except Exception as e:
                    print("could not post images", e)

            except Exception as e:
                print("could not fill ad details", e)

        except Exception as e:
            print("could not select sub-category", e)

    except Exception as e:
        print("could not select category", e)

    post.new_ad_page(WebDriverWait, EC)


x = 0
y = 0

while x < 20:
    price = "1200"
    random.shuffle(images_list)
    images = images_list[y:]
    description = random.choice(description_list) + "\n" + random.choice(description_list) + "\n" + random.choice(
        description_list) + "\n" + call_to_action
    title = get_title()
    create_new_post(driver, Keys, title, description, price, images, WebDriverWait, EC)
    x += 1
    y = random.randint(0, 35)
    print(f"{x} uploads completed")
