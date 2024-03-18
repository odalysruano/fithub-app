from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Routine(models.Model):
    day_of_the_week = models.CharField(max_length=50)
    focus_area = models.CharField(max_length=50)
    time_goal = models.IntegerField()
    calorie_goal = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.day_of_the_week
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'routine_id': self.id})
