import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class TestAmazonWeb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.get("http://www.amazon.com")
        assert "Amazon" in self.driver.title
        elem = self.driver.find_element_by_id("twotabsearchtextbox")
        elem.send_keys("javascript testing")
        elem.send_keys(Keys.RETURN)
        sleep(5)
        self.assertIn(u"\"javascript testing\"", self.driver.page_source)
