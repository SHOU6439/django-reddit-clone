from django.urls import path
from . import views

app_name = 'news_posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create-post/', views.CreatePostView.as_view(), name='create_post'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name="delete_post"),
    path('user-post-delete/<int:pk>/', views.DeleteLoginUserPostView.as_view(), name="delete_user_post"),
    path('post-detail/<int:pk>/', views.NewsPostDetailView.as_view(), name="post_detail"),
    path('create-comment/<int:pk>', views.CreateCommentView.as_view(), name="create_comment"),
    path('vote_up/<int:pk>', views.vote_up, name="vote_up"),
    path('vote_down/<int:pk>', views.vote_down, name="vote_down"),
    path('delete-comment/<int:pk>', views.DeleteCommentView.as_view(), name="delete_comment"),
    path('edit/<int:pk>', views.NewsPostEditView.as_view(), name='edit'),
    path('notification/<int:pk>', views.NotificationListView.as_view(), name="notification"),
    path('delete-notification/<int:pk>', views.DeleteNotificationView.as_view(), name="delete_notification"),
    path('create-replay/<int:pk>', views.CreateReplayView.as_view(), name="create_replay"),
    path('delete-replay/<int:pk>', views.DeleteReplayView.as_view(), name="delete_replay"),
    path('save/<int:pk>', views.SavePostView.as_view(), name="save"),
    path('unsave/<int:pk>', views.UnSavePostView.as_view(), name="unsave"),
]