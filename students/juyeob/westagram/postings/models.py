from django.db import models

from users.models import User

class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    contents = models.CharField(max_length=2000)
    created_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'posts'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    created_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'comments'


class like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'