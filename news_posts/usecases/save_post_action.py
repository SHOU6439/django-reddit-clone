from users.models import User, bookmarked_posts
from news_posts.models.news_posts import NewsPosts

def save_post_action(user: User, post: NewsPosts):
    user.saved_post.add(post)
    count_save = bookmarked_posts.objects.filter(post=post).count()
    post.save_counter = count_save
    post.save()