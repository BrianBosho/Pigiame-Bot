from selenium.webdriver.common.by import By


class CreateAd:
    def __init__(self, driver, keys, title, description, price, images):
        self.driver = driver
        self.Keys = keys
        self.title = title
        self.description = description
        self.price = price
        self.images = images

    def select_category(self):
        # create a variable with different categories so that  user select one from many categories.
        driver = self.driver
        home_category_button = driver.find_element_by_link_text("Home, Garden & Kids")
        home_category_button.click()
        decor_category = driver.find_element_by_link_text("Home Decor & Bedding")
        decor_category.click()

    def select_subcategory(self):
        # change this according to category being posted
        sub_categories = self.driver.find_elements_by_xpath(
            "//li[@data-post-listing-category-item='home-decor-bedding']/ul/li/a")
        # sub_categories[2].click() this is for curtains
        sub_categories[0].click()  # for carpets

    def fill_ad_details(self):
        driver = self.driver
        title = driver.find_element_by_name("title")
        title.send_keys(self.title)
        description = driver.find_element_by_name("description")
        description.send_keys(self.description)
        price = driver.find_element_by_name("price")
        price.send_keys(self.Keys.CONTROL + "a")
        price.send_keys(self.Keys.DELETE)
        price.send_keys(self.price)
        condition = driver.find_elements_by_class_name("custom-control-label")
        driver.execute_script("arguments[0].click();", condition[1])
        continue_button = driver.find_element_by_id("continue")
        continue_button.click()

    def upload(self, image):
        driver = self.driver
        uploader = driver.find_element_by_xpath("/html/body/input[1]")
        uploader.send_keys(image)


    def check_upload(self):
        driver = self.driver
        try:
            items = driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div/div[4]/div[3]/ul/li")
            print("Image uploaded", items)
            return True
        except Exception as e:
            print("Image failed to upload", e)
            return False

    def upload_images(self, images):
        driver = self.driver
        for x in range(12):
            self.upload(images[x])

        # state = not self.check_upload()
        # while state:
        #     driver.refresh()
        #     self.upload(image)
        #     state = not self.check_upload()

        next_button = driver.find_element_by_id("continue")
        driver.execute_script("arguments[0].click();", next_button)

    def select_product(self):
        #  pigiame package
        driver = self.driver
        driver.implicitly_wait(10)
        standard = driver.find_element_by_xpath("//input[@value='listing']")
        driver.execute_script("arguments[0].click();", standard)
        next_button = driver.find_element_by_id("continue")
        driver.execute_script("arguments[0].click();", next_button)

    def new_ad_page(self, WebDriverWait, EC):
        driver = self.driver
        driver.implicitly_wait(10)
        try:
            new_ad_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "CREATE AN AD")))
            driver.execute_script("arguments[0].click();", new_ad_button)
        except:
            driver.get("https://www.pigiame.co.ke/account/listing/create/classifieds?business=0")
            driver.refresh()
            new_ad_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "CREATE AN AD")))
            driver.execute_script("arguments[0].click();", new_ad_button)

        # new_ad_button = driver.find_element_by_link_text("CREATE AN AD")
        # driver.execute_script("arguments[0].click();", new_ad_button)
