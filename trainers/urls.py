from django.urls import path
from .views import welcome_trainer

urlpatterns = [
    path('', welcome_trainer, name='welcome_trainer')
]
