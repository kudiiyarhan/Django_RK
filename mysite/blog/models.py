from django.db import models


# создаем класс Article с полями
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=250)
    full_text = models.TextField()
    category = models.CharField(max_length=250)
    pubdate = models.DateTimeField()
    slug = models.CharField(max_length=255, unique=True)
    objects = models.Manager()
    # is_published = models.BooleanField() #TODO

    # меняем название тайтла в админке
    def __str__(self):
        return self.title

