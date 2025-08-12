from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('pub_date')
    context = {
        'books': books,
        'title': 'Каталог книг',
    }
    return render(request, template, context)

def book_by_date(request, pub_date):
    template = 'books/books_list.html'
    book_on_selected_date = Book.objects.filter(pub_date=pub_date)

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

    context = {
        'books': book_on_selected_date,
        'prev_day_books': prev_day_books,
        'next_day_books': next_day_books,
        'title': f'Книги на дату: {pub_date}',
    }
    return render(request, template, context)