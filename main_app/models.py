from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

EXERCISES = (
    ('A', 'Push-Ups'),
    ('B', 'Plank'),
    ('C', 'Squats'),
    ('D', 'Burpees'),
    ('E', 'Lunges'),
    ('F', 'Jumping Jacks'),
    ('G', 'Mountain Climbers'),
    ('H', 'Yoga'),
    ('I', 'Pilates'),
    ('J', 'Running'),
    ('K', 'Walking'),
)

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

class Exercise(models.Model):
    date = models.DateField('Exercise Date')
    name = models.CharField(
        max_length=1,
        choices=EXERCISES,
        default=EXERCISES[0][0]
    )
    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_name_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
