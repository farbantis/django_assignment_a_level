from django.urls import path, re_path
from .views import view_1, view_2, view_3, view_5, view_6, view_7, view_8, view_9, view_10, view_11


urlpatterns = [
    path('', view_1, name='main'),
    path('articles/', view_2),
    path('articles/archive/', view_3),
    path('users/', view_5),
    path('article/<int:article_number>/', view_6, name='article'),
    path('article/<int:article_number>/archive/', view_7),
    path('article/<int:article_number>/<slug:slug_text>/', view_8, name='article_and_slug'),
    path('users/<int:user_number>/', view_9),
    re_path(r'^(?P<data>[1-9a-f]{4}-[1-9a-zA-Z]{6})/$', view_10),
    re_path(r'^(?P<phone_num>[0](50|97|67|63|99|95)[0-9]{7})/$', view_11),
]

