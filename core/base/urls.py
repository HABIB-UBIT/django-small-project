from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.tweet_list, name= 'list'),
    path('list/', views.tweet_list, name='tweet_list'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('update/<str:pk>/', views.tweet_update, name='tweet_update'),
    path('delete/<str:pk>/', views.tweet_delete, name='tweet_delete'),
]