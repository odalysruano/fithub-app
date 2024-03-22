from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

EXERCISES = (
    ('A', 'Bench Press'),
    ('B', 'Biceps Curl'),
    ('C', 'Boxing'),
    ('D', 'Bridge'),
    ('E', 'Burpees'),
    ('F', 'Crunches'),
    ('G', 'Curtsy Lunge'),
    ('H', 'Cycling'),
    ('I', 'Dancing'),
    ('J', 'Deadlifts'),
    ('K', 'Donkey Kicks'),
    ('L', 'Dumbbell Curl'),
    ('M', 'Dumbbell Row'),
    ('N', 'Glute Bridge'),
    ('O', 'HIIT Workout'),
    ('P', 'Jump Rope'),
    ('Q', 'Jumping Jacks'),
    ('R', 'Lat Pulldown'),
    ('S', 'Leg Raise'),
    ('T', 'Lunges'),
    ('U', 'Mountain Climbers'),
    ('V', 'Overhead Press'),
    ('W', 'Pilates'),
    ('X', 'Planks'),
    ('Y', 'Pull-Ups'),
    ('Z', 'Push-Ups'),
    ('1', 'Reverse Lunge'),
    ('2', 'Running'),
    ('3', 'Russian Twist'),
    ('4', 'Sit-Ups'),
    ('5', 'Squats'),
    ('6', 'Step-Ups'),
    ('7', 'Stretching'),
    ('8', 'Superman'),
    ('9', 'Swimming'),
    ('0', 'Tricep Dips'),
    ('#', 'Walking'),
    ('!', 'Yoga'),
)

UPPER_EX = (
    ('Z', 'Push-Ups'),
    ('Y', 'Pull-Ups'),
    ('A', 'Bench Press'),
    ('V', 'Overhead Press'),
    ('B', 'Biceps Curl'),
    ('L', 'Dumbbell Curl'),
    ('M', 'Dumbbell Row'),
    ('0', 'Tricep Dips'),
    ('R', 'Lat Pulldown'),
    ('J', 'Deadlifts'),
    ('!', 'Yoga'),
    ('W', 'Pilates'),
    ('C', 'Boxing'),
)

LOWER_EX = (
    ('5', 'Squats'),
    ('J', 'Deadlifts'),
    ('T', 'Lunges'),
    ('1', 'Reverse Lunge'),
    ('G', 'Curtsy Lunge'),
    ('K', 'Donkey Kicks'),
    ('6', 'Step-Ups'),
    ('N', 'Glute Bridge'),
    ('!', 'Yoga'),
    ('W', 'Pilates'),
    ('2', 'Running'),
    ('#', 'Walking'),
    ('C', 'Boxing'),
)

CORE_EX = (
    ('X', 'Planks'),
    ('F', 'Crunches'),
    ('D', 'Bridge'),
    ('3', 'Russian Twist'),
    ('8', 'Superman'),
    ('4', 'Sit-Ups'),
    ('S', 'Leg Raise'),
    ('U', 'Mountain Climbers'),
    ('!', 'Yoga'),
    ('W', 'Pilates'),
    ('C', 'Boxing'),
)

CARDIO_EX = (
    ('2', 'Running'),
    ('I', 'Dancing'),
    ('Q', 'Jumping Jacks'),
    ('P', 'Jump Rope'),
    ('E', 'Burpees'),
    ('H', 'Cycling'),
    ('9', 'Swimming'),
    ('O', 'HIIT Workout'),
    ('C', 'Boxing'),
)

FLEX_EX = (
    ('!', 'Yoga'), 
    ('W', 'Pilates'), 
    ('#', 'Walking'), 
    ('7', 'Stretching'),
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

    user = models.ForeignKey(User, on_delete=models.CASCADE)

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
        choices=EXERCISES
    )
    sets = models.IntegerField(null=True, blank=True)
    reps = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_name_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
