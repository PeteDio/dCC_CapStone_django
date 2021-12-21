from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mealId = models.ForeignKey('meals.Meal', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    comment = models.CharField(max_length=300)