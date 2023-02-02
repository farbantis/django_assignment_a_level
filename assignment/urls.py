from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('app_1.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
