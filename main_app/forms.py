from django.forms import ModelForm, ChoiceField
from .models import Exercise, EXERCISES, UPPER_EX, LOWER_EX, CORE_EX, CARDIO_EX, FLEX_EX

class ExerciseForm(ModelForm):
    name = ChoiceField(choices=EXERCISES)
    
    class Meta:
        model = Exercise
        fields = ['date', 'name', 'sets', 'reps', 'weight']

    def __init__(self, *args, focus_area=None, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
        if focus_area:
            self.fields['name'].choices = self.get_filtered_choices(focus_area)

    def get_filtered_choices(self, focus_area):    
        if focus_area == '1':
            return UPPER_EX
        elif focus_area == '2':
            return LOWER_EX
        elif focus_area == '3':
            return CORE_EX
        elif focus_area == '4':
            return CARDIO_EX
        elif focus_area == '5':
            return FLEX_EX
