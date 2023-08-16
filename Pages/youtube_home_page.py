from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class YouTubeHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.youtube_search_bar = (By.ID, "search")
        self.youtube_search_bar_button = (By.ID, "search-icon-legacy")

    def go_to_youtube_home_page(self):
        self.driver.get("https://www.youtube.com")

    def enter_search_text(self, video_name):
        self.send_text(self.youtube_search_bar, video_name)
        self.click_function(self.youtube_search_bar_button)
