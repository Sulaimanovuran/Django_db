from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


from .models import *
from .forms import *

menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'Добавить новость', 'url_name': 'add_news'},
    {'title': 'Контакты', 'url_name': 'contact'},
    {'title': 'Выйти', 'url_name': 'logout'},
]


def index(request):
    news = News.objects.all()
    cats = Category.objects.all()
    context = {
        'menu':menu,
        'title': 'Главная страница',
        'news': news,
        'cats': cats,
        'cat_selected':0
    }
    return render(request, 'news/index.html', context=context)

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id) # News.objects.get(id=news_id) -> news
    cats = Category.objects.all()
    context = {
        'menu':menu,
        'title': 'Главная страница',
        'news': news,
        'cats': cats,
        'cat_selected':0
    }
    return render(request, 'news/news_detail.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST)
        if form.is_valid():
            try:
                News.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка при добавлении данных')
    else:
        form = AddNewsForm()
    return render(request, 'news/add_news.html', {'form': form, 'title': 'Добавить новость', 'menu': menu})


def contact(request):
    return HttpResponse('hello')

def logout(request):
    return HttpResponse('hello')