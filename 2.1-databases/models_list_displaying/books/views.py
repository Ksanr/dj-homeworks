from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {'books': books}
    return render(request, template, context)

def catalog_view(request):
    template = 'books/books_list_.html'
    context = {}
    return render(request, template, context)

def book_by_date(request, pub_date):
    template = 'books/book_by_date.html'
    book_on_selected_date = Book.objects.all().filter(pub_date=pub_date)

    prev_day_books = None
    next_day_books = None
    try:
        prev_day_books = max(Book.objects.filter(pub_date__lt=pub_date), key=lambda x:x.pub_date).pub_date
    except Exception as e:
        print(f'Error book: {e}')
        pass
    try:
        next_day_books = min(Book.objects.filter(pub_date__gt=pub_date), key=lambda x: x.pub_date).pub_date
    except Exception as e:
        print(f'Error book: {e}')
        pass
    print(prev_day_books, next_day_books)

    context = {
        'books': book_on_selected_date,
        'prev_day_books': prev_day_books,
        'next_day_books': next_day_books,

    }
    return render(request, template, context)