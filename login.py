from selenium import webdriver


class Login:
    def __init__(self, driver, account):
        self.account = account
        self.driver = driver

    def login(self):
        driver = self.driver
        driver.get("https://www.pigiame.co.ke/")
        driver.maximize_window()
        home_login_button = driver.find_element_by_css_selector("body > div.wrap > div.header-bar > div > div > a")
        home_login_button.click()
        username = driver.find_element_by_id("mobile_number")
        username.send_keys(self.account['mobile_no'])
        continue_button = driver.find_element_by_css_selector(
            "body > div.wrap > section > div > div:nth-child(1) > article > div > form > div.auth__submit > button")
        continue_button.click()
        password_input = driver.find_element_by_css_selector("#password")
        password_input.send_keys(self.account['password'])
        login_button = driver.find_element_by_xpath("/html/body/div[1]/section/div/div/article/div/form/div[3]/button")
        login_button.click()

    def click_cookie(self):
        driver = self.driver
        cookie_button = driver.find_element_by_css_selector(
            "body > div.js-cookie-consent.cookie-consent > div > div > div.cookie-consent__agree > button")
        cookie_button.click()

    def post_ad(self):
        self.click_cookie()
        driver = self.driver
        post_button = driver.find_element_by_link_text("Post Free Ad")
        post_button.click()
