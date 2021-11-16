from django.urls import path
from . import views

app_name = 'news_posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]