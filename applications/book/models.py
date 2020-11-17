from django.db import models
from applications.author.models import Author
# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.name

class Book(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE
    )
    authors = models.ManyToManyField(Author)
    title = models.CharField(
        max_length = 50 
    )
    date = models.DateField('Publication Date')
    cover_page = models.ImageField(upload_to = 'cover_page')
    views = models.PositiveIntegerField()

    def __str__(self):
        return self.title
