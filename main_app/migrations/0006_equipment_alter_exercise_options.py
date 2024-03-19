# Generated by Django 4.2.11 on 2024-03-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_exercise_reps_alter_exercise_sets_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['-date']},
        ),
    ]
