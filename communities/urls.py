from django.urls import path, include
from . import views



app_name="communities"
urlpatterns = [
    path('create-community/', views.CreateCommunityView.as_view(), name='create_community'),
]