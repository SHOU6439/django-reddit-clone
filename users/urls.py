from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



app_name="users"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', views.ProfileDetailView.as_view(), name='detail'),
    path('edit/', views.ProfileEditView.as_view(), name="edit"),
    path('saved-posts/<int:pk>', views.SavedPostDetailView.as_view(), name="saved_posts"),
    path('comments/<int:pk>', views.UsersCommentsView.as_view(), name="comments"),
    # path('up-voted-posts/<int:pk>', views.UserUpVotedPostsView.as_view(), name="up_voted_posts"),
    # path('down-voted-posts/<int:pk>', views.UserDownVotedPostsView.as_view(), name="down_voted_posts"),
    path('liked-posts/<int:pk>', views.UserLikedPostsView.as_view(), name="liked_posts")
]