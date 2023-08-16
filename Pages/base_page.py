from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_function(self, locator):
        try:
            element = WebElement.find_element(locator[0], locator[1])
            WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(element))
            element.click()
            print(f'Element with attribute type "{locator[0]}" and attribute value "{locator[1]}" click... SUCCESS!')
        except TimeoutException:
            print(f'Element with attribute type "{locator[0]}" and attribute value "{locator[1]}" click... FAILED!')
            raise

    def send_text(self, locator, input_text):
        try:
            element = WebElement.find_element(locator[0], locator[1])
            WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of(element))
            element.send_keys(input_text)
            print(f"Enter \"{input_text}\" text in input field... SUCCESS!")
        except TimeoutException:
            print(f"Enter \"{input_text}\" text in input field... FAILED!")
            raise

    def retrieve_title(self, page_title) -> str:
        WebDriverWait(self.driver, 30).until(expected_conditions.title_is(page_title))
        return self.driver.title
