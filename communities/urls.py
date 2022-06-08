from django.urls import path, include
from communities.views import *



app_name="communities"
urlpatterns = [
    path('create/', CreateCommunityView.as_view(), name='create'),
    path('detail/<int:pk>', CommunityDetailView.as_view(), name="detail"),
    path('join/<int:pk>', join, name="join"),
    path('leave/<int:pk>', leave, name="leave")
]