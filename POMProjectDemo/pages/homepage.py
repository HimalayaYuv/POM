class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_xpath = "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span"
        self.logout_link_xpath = "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"

    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome_link_xpath).click()

    def click_logout_link(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()
