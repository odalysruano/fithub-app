from django.db import models

# Create your models here.
class Routine(models.Model):
    day_of_the_week = models.CharField(max_length=50)
    focus_area = models.CharField(max_length=50)
    time_goal = models.IntegerField()
    calorie_goal = models.IntegerField()

    def __str__(self):
        return self.day_of_the_week
