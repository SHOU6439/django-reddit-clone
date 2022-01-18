from django.urls import path, include
from . import views



app_name="communities"
urlpatterns = [
    path('create/', views.CreateCommunityView.as_view(), name='create'),
    path('detail/<int:pk>', views.CommunityDetailView.as_view(), name="detail")
]