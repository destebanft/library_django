from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
# Create your views here.


class ListBooks(ListView):
    context_object_name = 'list_books'
    template_name = 'book/list.html'

    def get_queryset(self):
        key_word = self.request.GET.get('kword', '')
        #date_1
        d1 = self.request.GET.get('date_1', '')
        #date_2
        d2 = self.request.GET.get('date_2', '')

        if d1 and d2:
            return Book.objects.search_books2(key_word, d1, d2)
        else:
            return Book.objects.search_books(key_word)
