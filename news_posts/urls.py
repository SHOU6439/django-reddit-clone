from django.urls import path
from . import views

app_name = 'news_posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name="delete_post"),
    path('user-post-delete/<int:pk>/', views.DeleteLoginUserPostView.as_view(), name="delete_user_post"),
    path('post-detail/<int:pk>/', views.NewsPostDetailView.as_view(), name="post_detail"),
    path('create-comment/<int:pk>', views.CreateCommentView.as_view(), name="create_comment")
]