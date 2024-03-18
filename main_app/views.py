from django.shortcuts import render

routines = [
    {'day_of_the_week': 'monday', 'focus_area': 'arms', 'time_goal': 30, 'calories_goal': 200},
    {'day_of_the_week': 'tuesday', 'focus_area': 'legs', 'time_goal': 45, 'calories_goal': 250}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def routines_index(request):
    return render(request, 'routines/index.html', {
        'routines': routines
    })
