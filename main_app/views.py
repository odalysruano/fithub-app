from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Routine

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def routines_index(request):
    routines = Routine.objects.filter(user=request.user)
    return render(request, 'routines/index.html', {
        'routines': routines
    })

def routines_detail(request, routine_id):
    routine = Routine.objects.get(id=routine_id)
    return render(request, 'routines/detail.html', { 
        'routine': routine 
        })

class RoutineCreate(CreateView):
    model = Routine
    fields = '__all__'

class RoutineUpdate(UpdateView):
    model = Routine
    fields = ['focus_area', 'time_goal', 'calorie_goal']

class RoutineDelete(DeleteView):
    model = Routine
    success_url = '/routines'    

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
