class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        self.password_textbox_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        self.login_button_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
