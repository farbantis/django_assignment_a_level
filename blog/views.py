from django.db.models import Q
from django.shortcuts import render
from .models import Article, Comment, Author


def index(request):
    articles = Article.objects.\
        prefetch_related('author'). \
        prefetch_related('comment_set__author'). \
        prefetch_related('like_set').\
        prefetch_related('dislike_set').\
        all().order_by('-created_at')

    context = {
        'articles': articles,
    }
    return render(request, './blog.html', context)


def show_last_5_comments(request):
    # last_comments = Comment.objects.all().order_by('id')[:5][::-1]
    last_comments = Comment.objects.all().order_by('-created_at')[:5]
    context = {
        'last_comments': last_comments
    }
    return render(request, './last_5_comments.html', context)


def changing_comments_smf(request):
    # comments = Comment.objects.all()
    comments = Comment.objects.filter(
        Q(text__icontains='start') |
        Q(text__icontains='middle') |
        Q(text__icontains='finish')
    )
    for comment in comments:
        if 'start' in comment.text.lower() or 'middle' in comment.text.lower() or 'finish' in comment.text.lower():
            comment.text = 'THIS TEXT IS NOT ALLOWED HERE.'
    context = {'comments': comments}
    return render(request, './changing_comments_smf.html', context)


def delete_comments(request):
    comments = Comment.objects.filter(text__icontains='k').exclude(text__icontains='c')
    data = [x for x in comments]
    context = {'comments': data}
    comments.delete()
    return render(request, './delete_comments.html', context)


def get_2_comments(request):
    author = Author.objects.all().order_by('name')[:1]
    comments = Comment.objects.filter(author=author).order_by('-created_at')[:2]
    context = {'comments': comments}
    return render(request, './get_2_comments.html', context)
