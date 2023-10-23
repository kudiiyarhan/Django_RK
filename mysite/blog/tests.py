from django.test import TestCase
from  django.urls import resolve
from  .views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        '''тест проверяющий что при переходе на главную страницу открывается view под названием home_page'''

        found = resolve('/')
        self.assertEquals(found.func, home_page)


    def test_home_page_return_correct_html(self):
        '''тест проверяющий тайтл'''
        # создается объект запроса
        request = HttpRequest()
        # создается объект ответа на запрос с передачей страницы
        response = home_page(request)
        # создается переменная с декодированием ответа
        html = response.content.decode('utf8')

        # идет проверка на наличие тестовых данных в частях html страницы полученной после ответа
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Сайт Алексея Куличевского</title>', html)
        self.assertIn('<h1>Алексей Куличевский</h1>', html)
        self.assertTrue(html.endswith('</html>'))

