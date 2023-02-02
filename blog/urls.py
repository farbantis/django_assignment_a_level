from django.urls import path
from .views import index, show_last_5_comments, changing_comments_smf, delete_comments, get_2_comments


urlpatterns = [
    path('', index),
    path('last_comments/', show_last_5_comments),
    path('changing_comments_smf/', changing_comments_smf),
    path('delete_comments/', delete_comments),
    path('get_2_comments/', get_2_comments),
]
