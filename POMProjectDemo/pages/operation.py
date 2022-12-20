from POMProjectDemo.Locators.locators import Locator


class Operation():

    def __init__(self, driver):
        self.driver = driver

        self.admin_xpath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"
        self.job_xpath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
        self.pay_grades_link_text = "Pay Grades"
        self.add_button1_xpath = Locator.add_button1_xpath
        self.add_name_xpath = Locator.add_name_xpath
        self.name_save_xpath = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"

    def click_username(self):
        self.driver.find_element_by_xpath(self.admin_xpath).click()

    def click_job(self):
        self.driver.find_element_by_xpath(self.job_xpath).click()
        self.driver.find_element_by_link_text(self.pay_grades_link_text).click()

    def add_name(self, name):
        self.driver.find_element_by_xpath(self.add_button1_xpath).click()
        self.driver.find_element_by_xpath(self.add_name_xpath).clear()
        self.driver.find_element_by_xpath(self.add_name_xpath).send_keys(name)
        self.driver.find_element_by_xpath(self.name_save_xpath).click()

    def verify(self):
        self.driver.find_element_by_xpath(self.job_xpath).click()
        self.driver.find_element_by_link_text(self.pay_grades_link_text).click()
