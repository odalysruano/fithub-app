# Generated by Django 4.2.11 on 2024-03-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_equipment_alter_exercise_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='equipment',
            field=models.ManyToManyField(to='main_app.equipment'),
        ),
    ]
