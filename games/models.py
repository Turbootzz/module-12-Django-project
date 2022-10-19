from django.db import models

# Create your models here.


class Games(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    genre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/images/')

# admin panel
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:200]
