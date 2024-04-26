import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.form_data import FormData



def test_forms_positive():
    options = webdriver.ChromeOptions()

    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start Test")
    fd = FormData(driver)
    fd.positive()
    print("Finish Test")
    print("Позитивный тест прошел успешнo")
    driver.quit()



