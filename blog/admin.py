from django.contrib import admin
from .models import Author, Article, Comment, Like, DisLike, CommentSpecial, LikeToComment, DisLikeToComment

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
admin.site.register(LikeToComment)
admin.site.register(DisLikeToComment)
admin.site.register(CommentSpecial)

