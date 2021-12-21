from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Reply(models.Model):
    comments = models.ForeignKey('comments.Comment', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    userId=models.ForeignKey(User, on_delete=models.CASCADE)