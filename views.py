from django.shortcuts import render


# Create your views here.


def glavn_stran(request):
    title = 'Главная страница'
    lice_1 = 'Главная'
    lice_2 = 'Магазин'
    lice_3 = 'Корзина'
    context = {'title': title,
               'title_lice': lice_1,
               'shop': lice_2,
               'corzina': lice_3}
    return render(request, 'Glavn_stran.html', context)


def shop_stran(request):
    title = 'Магазин'
    games = ['Portal 3', 'Half life 3', 'Warcraft 4']
    lice_1 = 'Главная'
    lice_2 = 'Магазин'
    lice_3 = 'Корзина'
    context = {'title': title,
               'games': games,
               'title_lice': lice_1,
               'shop': lice_2,
               'corzina': lice_3}
    return render(request, 'Shop_stran.html', context)


def corzina_stran(request):
    title = 'Корзина'
    len_corz = 0
    lice_1 = 'Главная'
    lice_2 = 'Магазин'
    lice_3 = 'Корзина'
    context = {'title': title,
               'len_corz': len_corz,
               'title_lice': lice_1,
               'shop': lice_2,
               'corzina': lice_3}
    return render(request, 'Corzina.html', context)