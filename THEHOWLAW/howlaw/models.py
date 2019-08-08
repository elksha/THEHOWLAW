from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    img = models.FileField(null=True)
    name = models.CharField(max_length=200,)
    pwd = models.CharField(max_length=200,)
    post = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
<<<<<<< HEAD
    content = models.TextField()
=======
    content = models.TextField()
>>>>>>> 94f487ba733b0ce921c4220d6c0c04a220b324d3
