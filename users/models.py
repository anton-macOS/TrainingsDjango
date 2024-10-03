from django.db import models


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class UserStats(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    chest_circ = models.FloatField()
    waist_circ = models.FloatField()
    hip_circ = models.FloatField()

    def __str__(self):
        return f'{self.user_id}{self.user_id} | height: {self.height} | weight: {self.weight}'


