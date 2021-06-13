from django.db import models

class Link(models.Model):
    full_url = models.URLField(verbose_name='Полная ссылка', unique=False)
    short_url = models.URLField(verbose_name='Укороченная ссылка')
