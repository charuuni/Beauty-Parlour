from django.contrib import admin
from django.urls import path
from rest_framework import serializers
from.import views



urlpatterns = [
    path('Article_list/',views.Article_list,name='Article_list'),
    path('article_detail/<int:pk>/',views.article_detail,name='article_detail'),

    # path('Demo_list/',views.Demo_list,name='Demo_list'),
]