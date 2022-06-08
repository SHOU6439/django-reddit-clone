from django.urls import path
from chat.views import *



app_name="chat"

urlpatterns = [
    path('', ChatHomeView.as_view(), name="home"),
    path('dm/', ChatDMHomeView.as_view(), name="dm_home"),
    path('search/user/', SearchUserView.as_view(), name="search_user"),
    path('create/dm-room/<int:pk>', CreateDMRoomView.as_view(), name="create_dm_room"),
    path('dm/detail/<int:pk>', DMRoomDetailView.as_view(), name="dm_room_detail"),
    path('dm/invite/accept/<int:pk>', AcceptDMInviteView.as_view(), name="accept_dm_invite"),
    path('dm/invite/ignore/<int:pk>', IgnoreDMInviteView.as_view(), name="ignore_dm_invite"),
    path('dm/create/<int:pk>', CreateDirectMessageView.as_view(), name="create_dm")
]