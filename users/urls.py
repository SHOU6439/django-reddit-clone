from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



app_name="users"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', views.ProfileDetailView.as_view(), name='detail')
]