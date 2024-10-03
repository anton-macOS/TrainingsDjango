from django.urls import path
from .views import trainings
app_name = 'exercices'

urlpatterns = [
    path('', trainings, name='trainings')
]
