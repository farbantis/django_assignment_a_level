import datetime

from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='articles')
    text = models.TextField(max_length=10000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_at} by {self.author}'


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'by {self.author}'

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now() - datetime.timedelta(days=365)
        super(Comment, self).save(*args, **kwargs)


class LikeDislike(models.Model):
    user = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class Like(LikeDislike):
    """handles likes"""
    def __str__(self):
        return f'By user {self.user} to article {self.article}'


class DisLike(LikeDislike):
    """handles dislikes"""

    def __str__(self):
        return f'By user {self.user} to article {self.article}'
