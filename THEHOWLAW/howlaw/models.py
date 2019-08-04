from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200,)
    pwd = models.CharField(max_length=200,)
    post = models.TextField()
    # img = models.FileField(null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()