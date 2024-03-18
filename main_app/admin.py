from django.contrib import admin

from .models import Routine, Exercise

# Register your models here.
admin.site.register(Routine)
admin.site.register(Exercise)
