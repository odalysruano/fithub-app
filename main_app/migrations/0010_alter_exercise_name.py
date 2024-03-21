# Generated by Django 4.2.11 on 2024-03-21 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_routine_focus_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(choices=[('A', 'Push-Ups'), ('B', 'Pull-Ups'), ('C', 'Bench Press'), ('D', 'Overhead Press'), ('E', 'Biceps Curl'), ('F', 'Dumbbell Curl'), ('G', 'Dumbbell Row'), ('H', 'Tricep Dips'), ('I', 'Lat Pulldown'), ('J', 'Deadlifts'), ('K', 'Yoga'), ('L', 'Pilates'), ('M', 'Boxing'), ('A', 'Squats'), ('B', 'Deadlifts'), ('C', 'Lunges'), ('D', 'Reverse Lunge'), ('E', 'Curtsy Lunge'), ('F', 'Donkey Kicks'), ('G', 'Step-Ups'), ('H', 'Glute Bridge'), ('I', 'Yoga'), ('J', 'Pilates'), ('K', 'Running'), ('L', 'Walking'), ('M', 'Boxing'), ('A', 'Planks'), ('B', 'Crunches'), ('C', 'Bridge'), ('D', 'Russian Twist'), ('E', 'Superman'), ('F', 'Sit-Ups'), ('G', 'Leg Raise'), ('H', 'Mountain Climbers'), ('I', 'Yoga'), ('J', 'Pilates'), ('K', 'Boxing'), ('A', 'Running'), ('B', 'Dancing'), ('C', 'Jumping Jacks'), ('D', 'Jump Rope'), ('E', 'Burpees'), ('F', 'Cycling'), ('G', 'Swimming'), ('H', 'HIIT Workout'), ('I', 'Boxing'), ('A', 'Yoga'), ('B', 'Pilates'), ('C', 'Walking'), ('D', 'Stretching')], max_length=1),
        ),
    ]