from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page = {}
    page['number'] = max(int(request.GET.get('page', 1)), 1)
    if page['number'] > 1:
        page['has_previous'] = True
        page['previous_page_number'] = page['number'] - 1
    page['has_next'] = True
    page['next_page_number'] = page['number'] + 1
    stations = int(request.GET.get('stations', 10))
    start_station = stations * (page['number'] - 1) - 1
    finish_station = start_station + stations - 1
    context = {'bus_stations': []}

    with open('data-398-2018-08-30.csv', encoding='utf-8') as f:
        csv = DictReader(f)
        for i, line in enumerate(csv):
            if i > finish_station:
                break
            if i > start_station:
                context['bus_stations'].append(line)
        try:
            line = next(csv)
        except StopIteration:
            page['has_next'] = False

    context['page']= page
    return render(request, 'stations/index.html', context)
