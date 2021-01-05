from django.db import models
from django.db.models import Q

class AuthorManager(models.Manager):

    def search_authors(self, kword):
        result = self.filter(name__icontains=kword)
        return result

    def search_authors2(self, kword):
        result = self.filter(
            Q(name__icontains=kword) | Q(last_name__icontains=kword)
        )
        return result

    def search_authors3(self, kword):
        result = self.filter(name__icontains=kword).exclude(age=99)
        return result

    def search_authors4(self, kword):
        result = self.filter(
            age__gt=40,#mayor que
            age__lt=65#menor que
            ).order_by('last_name')
        return result
