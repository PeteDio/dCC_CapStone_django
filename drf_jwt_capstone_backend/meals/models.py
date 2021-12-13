from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()
    recipe = models.IntegerField()
    datetime = models.DateTimeField()
    caption = models.CharField(max_length=300)
