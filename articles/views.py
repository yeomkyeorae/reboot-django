from django.shortcuts import render, redirect
from .models import Articles

# Create your views here.
def main(request):
    return render(request, 'articles/main.html')



def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    articles = Articles(title=title, content=content)
    articles.save()

    return redirect('/articles/')


def detail(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    context = {
        'pk': article.pk,
        'title': article.title,
        'content': article.content,
        'created_at': article.created_at,
        'updated_at': article.updated_at,
    }

    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    article.delete()

    return redirect('/articles/')


def update(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    context = {
        'pk': article.pk,
        'title': article.title,
        'content': article.content,
    }

    return render(request, 'articles/update.html', context)


def updated(request, article_pk):
    article = Articles.objects.get(pk=article_pk)
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()

    return render(request, 'articles/updated.html')