from csv import DictReader

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))

def csv_to_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        data = [row for row in reader]
    return data

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    file_path = 'data-398-2018-08-30.csv'
    data = csv_to_dict(file_path)
    iter_per_page = 10 # int(request.GET.get('stations', 10))
    paginator = Paginator(data, iter_per_page)
    cur_page = int(request.GET.get('page', 1))
    page = paginator.get_page(cur_page)

    context = {
        'page': page,
        'bus_stations': page.object_list,
    }
    return render(request, 'stations/index.html', context)
