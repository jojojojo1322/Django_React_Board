#backend/post/models.py
from django.db import models
# from django.utils import timezone
from umc.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        """A string representation of the model."""
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE, related_name='comments')

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    objects = models.Manager()