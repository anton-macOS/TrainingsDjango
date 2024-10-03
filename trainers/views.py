from django.shortcuts import render
from .models import Trainer, Student
from exercises.models import Exercise

def welcome_trainer(request):
    trainer = Trainer.objects.filter(trainer_id=1).first()
    return render(request, 'trainers/trainers_main.html', {'trainer': trainer})


def students_list(request):
    my_students = Student.objects.filter(trainer_id=1)
    return render(request, 'trainers/students_list.html', {'list': my_students})


def create_training(request):
    my_students = Student.objects.filter(trainer_id=1)
    exercises = Exercise.objects.all()
    return render(request, 'trainers/create_training.html',
                  {'list': my_students, 'exercises': exercises})

