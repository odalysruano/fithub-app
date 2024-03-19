from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Routine
from .forms import ExerciseForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def routines_index(request):
    routines = Routine.objects.filter(user=request.user)
    return render(request, 'routines/index.html', {
        'routines': routines
    })

@login_required
def routines_detail(request, routine_id):
    routine = Routine.objects.get(id=routine_id)
    exercise_form = ExerciseForm()
    return render(request, 'routines/detail.html', { 
        'routine': routine,
        'exercise_form': exercise_form, 
        })

class RoutineCreate(LoginRequiredMixin, CreateView):
    model = Routine
    fields = ['day_of_the_week', 'focus_area', 'time_goal', 'calorie_goal']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class RoutineUpdate(LoginRequiredMixin, UpdateView):
    model = Routine
    fields = ['focus_area', 'time_goal', 'calorie_goal']

class RoutineDelete(LoginRequiredMixin, DeleteView):
    model = Routine
    success_url = '/routines'    

@login_required
def add_exercise(request, routine_id):
    form = ExerciseForm(request.POST)
    if form.is_valid():
        new_exercise = form.save(commit=False)
        new_exercise.routine_id = routine_id
        new_exercise.save()
    return redirect('detail', routine_id=routine_id)

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
