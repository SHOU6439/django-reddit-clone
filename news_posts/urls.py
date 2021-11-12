from django.urls import path
from . import views

app_name = 'news_posts'
urlpatterns = [
    path('', views.index, name='index')
]