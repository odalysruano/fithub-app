# Generated by Django 4.2.11 on 2024-03-18 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_routine_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Exercise Date')),
                ('name', models.CharField(choices=[('A', 'Push-Ups'), ('B', 'Plank'), ('C', 'Squats'), ('D', 'Burpees'), ('E', 'Lunges'), ('F', 'Jumping Jacks'), ('G', 'Mountain Climbers'), ('H', 'Yoga'), ('I', 'Pilates'), ('J', 'Running'), ('K', 'Walking')], default='A', max_length=1)),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.routine')),
            ],
        ),
    ]
