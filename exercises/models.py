from django.db import models


class Exercise(models.Model):
    exercise_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    muscle_type = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=100)
    video_example = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Exer.name: {self.name} id: {self.exercise_id}'


class Training(models.Model):
    training_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    notes = models.TextField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user_id} {self.training_id}'


class TrainingExercise(models.Model):
    training_id = models.ForeignKey('exercises.Training', on_delete=models.CASCADE)
    exercise_id = models.ForeignKey('exercises.Exercise', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return f'{self.exercise_id}'
