from django.shortcuts import render
from .models import Article, Comment


def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, './blog.html', context)

def show_last_5_comments(request):
    last_comments = Comment.objects.all().order_by('id')[:5][::-1]
    context = {
        'last_comments': last_comments
    }
    return render(request, './last_5_comments.html', context)