from django.db import models
from django.db.models import Q

class BookManager(models.Manager):

    def search_books(self, kword):
        result = self.filter(
            title__icontains=kword,
            #date__range=('1000-01-01', '1980-01-01')
            )
        return result

    def search_books2(self, kword, date_1, date_2):
        result = self.filter(
            title__icontains=kword,
            date__range=(date_1, date_2)
            )
        return result
