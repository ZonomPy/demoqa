import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.form_data import FormData



def test_forms_negative():
    options = webdriver.ChromeOptions()

    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    print("Start Test")
    fd = FormData(driver)
    fd.negative()
    print("Finish Test")
    print("Негативный тест прошел успешон")
    driver.quit()



