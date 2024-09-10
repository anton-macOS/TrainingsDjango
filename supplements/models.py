from django.db import models
from users.models import User


class Supplements(models.Model):
    supplements_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    supplements = models.TextField()
