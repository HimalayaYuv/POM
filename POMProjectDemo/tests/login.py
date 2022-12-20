import unittest
from time import sleep

from selenium import webdriver

from POMProjectDemo.pages.homepage import HomePage
from POMProjectDemo.pages.loginpage import LoginPage
from POMProjectDemo.pages.operation import Operation


class LoginTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        sleep(5)

        operation = Operation(driver)

        operation.click_username()
        sleep(5)
        operation.click_job()
        sleep(5)
        operation.add_name("grade 500000")
        sleep(5)
        operation.verify()
        sleep(5)

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout_link()

        sleep(5)
        # self.driver.find_element_by_xpath(
        #     '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
        # self.driver.find_element_by_xpath(
        #     '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
        # self.driver.find_element_by_xpath(
        #     '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        # sleep(5)
        # self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span').click()
        # self.driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
        # sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")
