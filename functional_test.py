from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By

class BasicInstallTest(unittest.TestCase):
    # Жил был Вася.
    # Вася работает аналитиком в какой-то кампании
    # Однажды Вася захотел прокачать знания в аналитике
    # Вася зашел в гугл и ввел запрос 'Когортный анализ'


    def setUp(self):
        '''функция создания объекта browser'''

        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''функция закрытия браузера по завершении'''

        self.browser.quit()

    # В браузере Васи открылся сайт по адресу http://127.0.0.1:8000
    # В заголовке сайта Вася прочитал 'Сайт Алексея Куличевского'
    def test_home_page_title(self):
        '''тест наличия слова на главной странице в тайтле.'''


        self.browser.get('http://127.0.0.1:8000')
        self.assertIn('Сайт Алексея Куличевского', self.browser.title)



    # В шапке сайта написано 'Алексей Куличевский'
    def test_home_page_header(self):
        '''тест наличия текста (Алексей Куличевский) в заголовке сайта'''


        self.browser.get('http://127.0.0.1:8000')
        header = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Алексей Куличевский', header)


    # Под шапкой расположен блог со статьями
    def test_home_page_blog(self):
        '''тест блока блог'''
        self.browser.get('http://127.0.0.1:8000')
        article_list = self.browser.find_element(By.CLASS_NAME, 'article-list')
        self.assertTrue(article_list)


    # У каждой статьи есть заголовок и один абзац с текстом
    def test_home_page_articles_look_correct(self):
        '''тест проверяющий наличие заголовка и статьи в блоге'''
        self.browser.get('http://127.0.0.1:8000')
        article_title = self.browser.find_element(By.CLASS_NAME, 'article-title')
        article_summary = self.browser.find_element(By.CLASS_NAME, 'article-summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)






if __name__ == '__main__':
    unittest.main()



# Жил был Вася.
# Вася работает аналитиком в какой-то кампании
# Однажды Вася захотел прокачать знания в аналитике
# Вася зашел в гугл и ввел запрос 'Когортный анализ'
# В браузере Васи открылся сайт по адресу ...
# В заголовке сайта Вася прочитал 'Сайт Алексея Куличевского'
# В шапке сайта написано 'Алексей Куличевский'
# Под шапкой расположен блог со статьями
# У каждой статьи есть заголовок и один абзац с текстом
# Вася кликнул по заголовку и у него открылась страница с полным текстом статьи
# Прочитав статью Вася кликнул по тексту 'Алексей Куличевский' и попал на главную страницу
