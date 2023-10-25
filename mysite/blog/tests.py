from django.test import TestCase
from django.urls import resolve
from .views import home_page
from .models import Article
from django.http import HttpRequest
from datetime import datetime


# тест проверяющий домашнюю страницу
class HomePageTest(TestCase):

    def test_home_page_displays_articles(self):
        '''тест проверяет наличие на главной странице статей и тайтла с заголовком'''
        Article.objects.create(
            title='title 1',
            summary='summary 1',
            full_text='full_text 1',
            pubdate=datetime.now()
        )

        Article.objects.create(
            title='title 2',
            summary='summary 2',
            full_text='full_text 2',
            pubdate=datetime.now()
        )

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertIn('title 1', html)
        self.assertIn('summary 1', html)
        self.assertNotIn('full_text 1', html)

        self.assertIn('title 2', html)
        self.assertIn('summary 2', html)
        self.assertNotIn('full_text 2', html)



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


# создает класс тестирования блога
class ArticleModelTest(TestCase):

    def test_article_model_save_and_retrieve(self):
        '''тест на создание и загрузку статей'''


        # создай статью 1
        # сохрани статью 1 в базе
        article1 = Article(
            title='article 1',
            full_text='full_text 1',
            summary='summaru 1',
            category='category 1',
            pubdate=datetime.now())
        article1.save()

        # создай статью 2
        # сохрани статью 2 в базе
        article2 = Article(
            title='article 2',
            full_text='full_text 2',
            summary='summaru 2',
            category='category 2',
            pubdate=datetime.now())
        article2.save()

        # загрузи из базы все статьи
        all_articles = Article.objects.all()

        # проверь: статей должно быть 2
        self.assertEqual(len(all_articles), 2)
        # проверь: 1 загруженная из базы статья == статья 1
        self.assertEqual(all_articles[0].title, article1.title)
        # проверь: 2 загруженная из базы статья == статья 2
        self.assertEqual(all_articles[1].title, article2.title)