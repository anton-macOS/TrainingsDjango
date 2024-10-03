from django.shortcuts import render
from .models import Training, TrainingExercise


def trainings(request):
    user_trainings = Training.objects.filter(user_id=1)
    user_exercises = TrainingExercise.objects.filter(training_id__in=user_trainings)
    print(user_trainings)
    print(user_exercises)
    return render(request, 'users/trainings.html',
                  {'user_trainings': user_trainings, 'user_exercises': user_exercises})
