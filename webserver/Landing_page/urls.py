# Urls for Landing_page
from django.urls import path
from django.contrib import admin
from django.urls import re_path
from rest_framework.authtoken import views

from .views import HelloWorld, test_view, matches, test_matches, TokenViewTest, get_tables

urlpatterns = [
    path('tests/', test_view, name='test_view'),
    path('matches/', matches, name='matches'),
    path('test_matches/', test_matches, name='test_matches'),
    path('hello_world', HelloWorld.as_view()),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    # Paths for login
    path('test_token/',TokenViewTest.as_view()),
    path('tables/', get_tables, name='get_tables'),
] 

