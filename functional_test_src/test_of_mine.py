# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get('http://127.0.0.1:8000/')
# assert 'My Cook Django Site' in browser.title
# print (browser.title)
# browser.quit()

import unittest
from selenium import webdriver


class FindElement(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def test_finding_element(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000/')
        self.assertIn('My Cook Django Site', browser.title)

    def test_registration(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000')
        element = browser.find_element_by_class_name('form-control')
        element.send_keys('Dimonda')
        element.submit()

    def testAssertion(self):
        browser = self.browser
        browser.get('http://127.0.0.1:8000')
        self.assertIn('Letitsell', browser.find_element_by_class_name('navbar-brand'))

    def tearDown(self):
        self.browser.close()


if __name__ == '__main__':
    unittest.main()
