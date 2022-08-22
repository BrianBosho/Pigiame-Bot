class ManageAds:
    def __init__(self, driver, keys, ec, web_driver_wait):
        self.driver = driver
        self.keys = keys
        self.WebDriverWait = web_driver_wait
        self.EC = ec

    def open_manage_ads_page(self):
        driver = self.driver
        driver.implicitly_wait(10)
        manage_button = driver.find_element_by_link_text("MANAGE MY ADS")
        manage_button.click()

    def open_drafts(self):
        driver = self.driver
        driver.implicitly_wait(10)
        # drafts_button = driver.find_element_by_link_text(" Drafts ")
        drafts_button = driver.find_element_by_id("state-drafts")
        drafts_button.click()
        driver.implicitly_wait(60)

    def action_dropdown(self):
        driver = self.driver
        driver.implicitly_wait(10)
        actions_buttons = driver.find_elements_by_class_name("workflow-manage")
        actions_buttons[0].click()

    def delete_action(self):
        driver = self.driver
        buttons = driver.find_elements_by_xpath(
            "/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div[5]/div/ul/li[1]/div/div[2]/div/div[2]/div/div/div/a")
        delete_button = buttons[2]

        def check_timeout():
            try:
                self.WebDriverWait(driver, 10).until(self.EC.alert_is_present())
                print("no timeout")

            except Exception as e:
                print("Time out retyring... ", e)
                self.delete_action()

        def check_alert():
            check_timeout()
            try:
                driver.switch_to.alert.accept()
                print("alert accepted")
                return True
            except Exception as e:
                print("No pop up, retrying ", e)
                return False

        def delete():
            try:
                delete_button.click()
                print("delete clicked")
                driver.implicitly_wait(5)
            except Exception as e:
                print("Element not found", e)
                self.action_dropdown()
                self.delete_action()

        delete()
        alert_state = check_alert()
        no_popup = not alert_state

        while no_popup:
            delete()
            alert_state = check_alert()
            no_popup = not alert_state

    # def open_online(self):
    #     driver = self.driver
    #     driver.implicitly_wait(10)
    #     online_button = driver.find_element_by_link_text("Online")
    #     online_button.click()
    #
    def open_offline(self):
        driver = self.driver
        driver.implicitly_wait(10)
        offline_button = driver.find_element_by_id("state-offline")
        offline_button.click()

    def open_rejected(self):
        driver = self.driver
        driver.implicitly_wait(10)
        rejected_button = driver.find_element_by_id("state-rejected")
        rejected_button.click()
