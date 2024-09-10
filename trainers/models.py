from django.db import models
from users.models import User


class Trainer(models.Model):
    trainer_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Student: {self.user_id} | Trainer: {self.trainer_id}'
