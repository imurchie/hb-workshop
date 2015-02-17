import os
import sys
import httplib
import base64
import json
import new
import unittest
import sauceclient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sauceclient import SauceClient
from time import sleep


USERNAME = os.environ.get('SAUCE_USERNAME')
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
sauce = SauceClient(USERNAME, ACCESS_KEY)

browsers = [{
                "platform": "OS X 10.10",
                "browserName": "chrome",
                "version": "38"
            },
            {
                "platform": "OS X 10.10",
                "browserName": "Safari",
                "version": "8.0"
            },
            {
                "platform": "Windows 8.1",
                "browserName": "internet explorer",
                "version": "11"
            },]


def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator


@on_platforms(browsers)
class TestAmazonWebSauce(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()

        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (USERNAME, ACCESS_KEY)
        )
        self.driver.implicitly_wait(30)


    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()


    def test_sauce(self):
        self.driver.get("http://www.amazon.com")
        assert "Amazon" in self.driver.title
        elem = self.driver.find_element_by_id("twotabsearchtextbox")
        elem.send_keys("javascript testing")
        #submit = self.driver.find_element_by_css_selector(".nav-submit-input")
        #submit.click()
        #sleep(5)
        elem.send_keys(Keys.ENTER)
        sleep(2)
        self.assertIn(u"\"javascript testing\"", self.driver.page_source)
