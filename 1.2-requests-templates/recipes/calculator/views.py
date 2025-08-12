from django.http import HttpResponse
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

def calc_ingredients(recipe: str, person: int):
    return {key: value * person for key, value in DATA[recipe].items()}

def recipe_view(request, rec):
    count = int(request.GET.get('servings', 1))
    if rec in DATA:
        recipe = calc_ingredients(rec, count)
    else:
        return HttpResponse('Такого рецепта нет в базе данных')
    pages = {
        'Главная страница': reverse('home'),
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('buter'),
    }
    context = {
        'recipe': recipe,
        'pages': pages
    }

    return render(request, 'calculator/index.html', context)
