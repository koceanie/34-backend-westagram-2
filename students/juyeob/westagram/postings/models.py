from django.db import models

from users.models import User

class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200, null=True)
    contents = models.CharField(max_length=2000)
    created_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'posts'

    #데이터베이스 다시생성해야함


class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'comments'


class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'