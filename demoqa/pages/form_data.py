from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

from base.base_class import Base


class Locators:
    full_name = "//input[@id='userName']"
    email = "//input[@id='userEmail']"
    current_address = "//textarea[@id='currentAddress']"
    permanent_address = "//textarea[@id='permanentAddress']"
    submit_button = "//button[@id='submit']"
    result_full_name = "//p[@id='name']"
    result_email = "//p[@id='email']"
    result_cur_address = "//p[@id='currentAddress']"
    result_per_address = "//p[@id='permanentAddress']"


class FormData(Base):
    url = 'https://demoqa.com/text-box'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.faker = Faker()

    ## Getters

    def wait_and_get_element(self, locator):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, locator)))

    def get_full_name(self):
        return self.wait_and_get_element(Locators.full_name)

    def get_email(self):
        return self.wait_and_get_element(Locators.email)

    def get_current_address(self):
        return self.wait_and_get_element(Locators.current_address)

    def get_permanent_address(self):
        return self.wait_and_get_element(Locators.permanent_address)

    def get_submit_button(self):
        return self.wait_and_get_element(Locators.submit_button)

    def get_result_full_name(self):
        return self.wait_and_get_element(Locators.result_full_name)

    def get_result_email(self):
        return self.wait_and_get_element(Locators.result_email)

    def get_result_cur_address(self):
        return self.wait_and_get_element(Locators.result_cur_address)

    def get_result_per_address(self):
        return self.wait_and_get_element(Locators.result_per_address)

    ## Actions
    def get_full_name_text(self):
        full_name_text = self.get_result_full_name().text.split(":")[1]
        return full_name_text

    def get_email_text(self):
        email_text = self.get_result_email().text.split(":")[1]
        return email_text

    def get_cur_address_text(self):
        address_text = self.get_result_cur_address().text.split(":")[1]
        return address_text

    def get_per_address_text(self):
        per_address_text = self.get_result_per_address().text.split(":")[1]
        return per_address_text

    def input_full_name(self, full_name):
        self.get_full_name().send_keys(full_name)

    def input_email(self, email):
        self.get_email().send_keys(email)

    def input_current_address(self, current_address):
        self.get_current_address().send_keys(current_address)

    def input_permanent_address(self, permanent_address):
        self.get_permanent_address().send_keys(permanent_address)

    def click_submit_button(self):
        self.get_submit_button().click()

    def positive(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        entered_full_name = self.faker.first_name()
        entered_email = self.faker.email()
        entered_current_address = self.faker.street_address()
        entered_permanent_address = self.faker.street_address()
        self.input_full_name(entered_full_name)
        self.input_email(entered_email)
        self.input_current_address(entered_current_address)
        self.input_permanent_address(entered_permanent_address)
        self.scroll_page(0, 300)
        self.click_submit_button()
        self.check_word(self.get_full_name_text(), entered_full_name)
        self.check_word(self.get_email_text(), entered_email)
        self.check_word(self.get_cur_address_text(), entered_current_address)
        self.check_word(self.get_per_address_text(), entered_permanent_address)

    def negative(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        entered_full_name = self.faker.first_name()
        entered_email = self.faker.email()
        entered_current_address = self.faker.street_address()
        entered_permanent_address = self.faker.street_address()
        self.input_full_name(" ")
        self.input_email(entered_email)
        self.input_current_address(entered_current_address)
        self.input_permanent_address(entered_permanent_address)
        self.scroll_page(0, 300)
        self.click_submit_button()
        self.check_word(self.get_email_text(), entered_email)
        self.check_word(self.get_cur_address_text(), entered_current_address)
        self.check_word(self.get_per_address_text(), entered_permanent_address)
