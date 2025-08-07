from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter'),
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def omlet_view(request):
    count = request.GET.get('servings', 1)
    context = {'recipe': {}}
    for key, item in DATA['omlet'].items():
        context['recipe'][key] = item * int(count)
    return render(request, 'calculator/index.html', context)

def pasta_view(request):
    count = request.GET.get('servings', 1)
    context = {'recipe': {}}
    for key, item in DATA['pasta'].items():
        context['recipe'][key] = item * int(count)
    return render(request, 'calculator/index.html', context)

def buter_view(request):
    count = request.GET.get('servings', 1)
    context = {'recipe': {}}
    for key, item in DATA['buter'].items():
        context['recipe'][key] = item * int(count)
    return render(request, 'calculator/index.html', context)