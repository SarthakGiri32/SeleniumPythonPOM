from selenium import webdriver

from Pages.youtube_home_page import YouTubeHomePage


class YoutubeAutomationTest:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.home_page = YouTubeHomePage(self.driver)

    def test_method(self):
        self.home_page.go_to_youtube_home_page()
        self.home_page.enter_search_text("Python tutorials")


youtube_automation_test = YoutubeAutomationTest()
youtube_automation_test.test_method()
