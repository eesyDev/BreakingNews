from django.shortcuts import render, redirect
from .models import Category, News, Like
from .weather import get_weather


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    weather = get_weather()
    context = {
        'news': news,
        'categories': categories, 
        'weather': weather
    }
    return render(request, 'index.html', context=context)


def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    news.views += 1
    news.save()
    news.refresh_from_db()
    return render(request, 'news_detail.html', context={'n': news})


def get_news_category(request, slug):
    news = News.objects.filter(category__slug=slug)
    context = {
        'news': news,
    }
    return render(request, 'index.html', context=context)

def show_weather(request):
    weather = get_weather()
    return render(request, 'index.html', context={'weather': weather})


def like_view(user, news):
    like = Like.objects.filter(user=user, news=news).exists()
    if not like:
        like = Like.objects.create(user=user, news=news)
        like.save()
        news.likes += 1
        news.save()
    else:
        Like.objects.get(user=user, news=news).delete()
        news.likes -= 1
        news.save()

def news_like(request, news_id):
    news = News.objects.get(id=news_id)
    user = request.user
    like_view(user=user, news=news)
    return redirect('/')

def news_like_detail(request, news_id):
    news = News.objects.get(id=news_id)
    user = request.user
    like_view(user=user, news=news)
    return render(request, 'news_detail.html', context={'n': news})