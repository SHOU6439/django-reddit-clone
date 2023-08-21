from inspect import _void
from django.db.models import Sum, Q
from news_posts.models.news_posts import NewsPosts


def post_like_state_highlight(context: dict, current_user: int, post_list_name: str, queryset: NewsPosts) -> _void:
    if current_user is None:
        # 未ログイン時の処理
        context[post_list_name] = queryset.annotate(
            like_count=Sum('liked_post__is_liked')
        )
    else:
        # ログイン時の処理
        # vote_stateにはログインユーザーの投票状態が入る
        context[post_list_name] = queryset.annotate(
            like_count=Sum('liked_post__is_liked'),
            like_state=Sum('liked_post__is_liked',
                filter=Q(liked_post__liked_user_id=current_user)
            )
        )
