from django.contrib import admin
from exercises.models import Exercise, Training, TrainingExercise

admin.site.register(Exercise)
admin.site.register(Training)
admin.site.register(TrainingExercise)
