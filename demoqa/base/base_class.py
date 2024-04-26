from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def scroll_page(self, x, y):
        """Скроллинг экрана"""
        return self.driver.execute_script(f"window.scrollTo({x},{y})")

    def check_word(self, word, result):
        """Проверка на корректность ввода и вывода"""
        assert word == result
        print("Проверка прошла успешнo")
