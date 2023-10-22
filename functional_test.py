from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class BasicInstallTest(unittest.TestCase):


    def setUp(self):
        '''функция создания объекта browser'''

        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''функция закрытия браузера по завершении'''

        self.browser.quit()

    def test_install(self):
        '''тест наличия слова на главной странице в тайтле.'''

        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Congratulations', self.browser.title)



if __name__ == '__main__':
    unittest.main()
