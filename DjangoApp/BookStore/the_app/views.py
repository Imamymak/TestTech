from .models import Book
from django.shortcuts import render


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


