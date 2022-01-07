from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Meal(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    likes = models.IntegerField()
    recipe = models.URLField(max_length=200)
    date = models.DateField()
    caption = models.CharField(max_length=300)
