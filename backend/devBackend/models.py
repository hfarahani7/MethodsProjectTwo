from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=60)
    caption = models.CharField(max_length=120)
    def __str__(self):
        return self.title