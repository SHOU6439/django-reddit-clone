from django.urls import path
from . import views



app_name="chat"

urlpatterns = [
    path('', views.ChatHomeView.as_view(), name="home"),
    path('dm/', views.ChatDMHomeView.as_view(), name="dm_home"),
    path('search/user/', views.SearchUserView.as_view(), name="search_user"),
    path('create/dm-room/<int:pk>', views.CreateDMRoomView.as_view(), name="create_dm_room"),
    path('dm/detail/<int:pk>', views.DMRoomDetailView.as_view(), name="dm_room_detail"),
    path('dm/invite/accept/<int:pk>', views.AcceptDMInviteView.as_view(), name="accept_dm_invite"),
    path('dm/invite/ignore/<int:pk>', views.IgnoreDMInviteView.as_view(), name="ignore_dm_invite"),
    path('dm/create/<int:pk>', views.CreateDirectMessageView.as_view(), name="create_dm")
]