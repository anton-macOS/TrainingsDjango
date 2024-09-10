from django.db import models
from users.models import User


class Exercise(models.Model):
    exercise_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    muscle_type = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=100)
    video_example = models.URLField(max_length=255, blank=True, null=True)


class Training(models.Model):
    training_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()
    status = models.CharField(max_length=10)


class TrainingExercise(models.Model):
    training_id = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sets = models.IntegerField()
