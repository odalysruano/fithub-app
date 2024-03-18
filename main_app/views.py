from django.shortcuts import render

from .models import Routine

routines = [
    {'day_of_the_week': 'monday', 'focus_area': 'arms', 'time_goal': 30, 'calorie_goal': 200},
    {'day_of_the_week': 'tuesday', 'focus_area': 'legs', 'time_goal': 45, 'calorie_goal': 250}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def routines_index(request):
    routines = Routine.objects.all()
    return render(request, 'routines/index.html', {
        'routines': routines
    })
