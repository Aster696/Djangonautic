from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about', views.aboutPage),
    path('articles/', include('articles.urls')),
]
