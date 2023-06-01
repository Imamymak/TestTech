from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    editor = models.CharField(max_length=50)
    language = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)