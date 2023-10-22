from django.test import TestCase
from  django.urls import resolve
from  .views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        '''тест проверяющий что при переходе на главную страницу открывается view под названием home_page'''

        found = resolve('/')
        self.assertEquals(found.func, home_page)


    def test_home_page_return_correct_html(self):
        pass