from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet

def search_user_action(q) -> QuerySet:
    object_list = get_user_model().objects.filter(username__icontains=q).order_by('-created_at')
    return object_list