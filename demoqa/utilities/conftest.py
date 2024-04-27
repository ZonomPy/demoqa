import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_up():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    url = 'https://demoqa.com/text-box'
    driver.get(url)
    driver.maximize_window()
    print("Start test")
    yield driver
    driver.quit()
    print("End test")
