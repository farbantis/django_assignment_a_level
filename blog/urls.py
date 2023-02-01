from django.urls import path
from .views import index, show_last_5_comments


urlpatterns = [
    path('', index),
    path('last_comments', show_last_5_comments),

]