from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

UPPER_EX = (
    ('A', 'Push-Ups'),
    ('B', 'Pull-Ups'),
    ('C', 'Bench Press'),
    ('D', 'Overhead Press'),
    ('E', 'Biceps Curl'),
    ('F', 'Dumbbell Curl'),
    ('G', 'Dumbbell Row'),
    ('H', 'Tricep Dips'),
    ('I', 'Lat Pulldown'),
    ('J', 'Deadlifts'),
    ('K', 'Yoga'),
    ('L', 'Pilates'),
    ('M', 'Boxing'),
)

LOWER_EX = (
    ('A', 'Squats'),
    ('B', 'Deadlifts'),
    ('C', 'Lunges'),
    ('D', 'Reverse Lunge'),
    ('E', 'Curtsy Lunge'),
    ('F', 'Donkey Kicks'),
    ('G', 'Step-Ups'),
    ('H', 'Glute Bridge'),
    ('I', 'Yoga'),
    ('J', 'Pilates'),
    ('K', 'Running'),
    ('L', 'Walking'),
    ('M', 'Boxing'),
)

CORE_EX = (
    ('A', 'Planks'),
    ('B', 'Crunches'),
    ('C', 'Bridge'),
    ('D', 'Russian Twist'),
    ('E', 'Superman'),
    ('F', 'Sit-Ups'),
    ('G', 'Leg Raise'),
    ('H', 'Mountain Climbers'),
    ('I', 'Yoga'),
    ('J', 'Pilates'),
    ('K', 'Boxing'),
)

CARDIO_EX = (
    ('A', 'Running'),
    ('B', 'Dancing'),
    ('C', 'Jumping Jacks'),
    ('D', 'Jump Rope'),
    ('E', 'Burpees'),
    ('F', 'Cycling'),
    ('G', 'Swimming'),
    ('H', 'HIIT Workout'),
    ('I', 'Boxing'),
)

FLEX_EX = (
    ('A', 'Yoga'),
    ('B', 'Pilates'),
    ('C', 'Walking'),
    ('D', 'Stretching'),
)

FOCUS = (
    ('1', 'Upper Body'),
    ('2', 'Lower Body'),
    ('3', 'Core'),
    ('4', 'Cardio'),
    ('5', 'Flexibility'),
)

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('equipments_detail', kwargs={'pk': self.id})

class Routine(models.Model):
    day_of_the_week = models.CharField(max_length=50)
    focus_area = models.CharField(
        max_length=1,
        choices=FOCUS,
        default=FOCUS[0][0]
    )
    time_goal = models.IntegerField()
    calorie_goal = models.IntegerField()

    equipments = models.ManyToManyField(Equipment)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_focus_area_display()
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'routine_id': self.id})

class Exercise(models.Model):
    date = models.DateField('Exercise Date')
    name = models.CharField(
        max_length=1,
        choices=UPPER_EX + LOWER_EX + CORE_EX + CARDIO_EX + FLEX_EX,
    )
    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_name_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
