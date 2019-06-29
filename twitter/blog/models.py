from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.TextField()


    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'