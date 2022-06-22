from django.urls import path
from news_posts.views import *

app_name = 'news_posts'
urlpatterns = [
    path('', HotIndexView.as_view(), name='hot_index'),
    path('new/', NewIndexView.as_view(), name='new_index'),
    path('liked/', LikedIndexView.as_view(), name='liked_index'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name="delete_post"),
    path('user-post-delete/<int:pk>/', DeleteLoginUserPostView.as_view(), name="delete_user_post"),
    path('post-detail/<int:pk>/', NewsPostDetailView.as_view(), name="post_detail"),
    path('create-comment/<int:pk>', CreateCommentView.as_view(), name="create_comment"),
    # path('vote_up/<int:pk>', vote_up, name="vote_up"),
    # path('vote_down/<int:pk>', vote_down, name="vote_down"),
    path('like/<int:pk>', like, name='like'),
    path('delete-comment/<int:pk>', DeleteCommentView.as_view(), name="delete_comment"),
    path('edit/<int:pk>', NewsPostEditView.as_view(), name='edit'),
    path('notification/<int:pk>', NotificationListView.as_view(), name="notification"),
    path('delete-notification/<int:pk>', DeleteNotificationView.as_view(), name="delete_notification"),
    path('create-replay/<int:pk>', CreateReplayView.as_view(), name="create_replay"),
    path('delete-replay/<int:pk>', DeleteReplayView.as_view(), name="delete_replay"),
    path('save/<int:pk>', SavePostView.as_view(), name="save"),
    path('unsave/<int:pk>', UnSavePostView.as_view(), name="unsave"),
]