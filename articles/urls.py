from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list),
    path('/<int: param>/', views.article_details)
]
