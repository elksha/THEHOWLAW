from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
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
    content = models.TextField()
>>>>>>> 092fff9cdfd52088a1fd30774dd6105137da367e
