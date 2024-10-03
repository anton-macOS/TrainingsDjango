from django.urls import path
from .views import welcome_trainer, students_list, create_training
app_name = 'trainers'
urlpatterns = [
    path('', welcome_trainer, name='welcome_trainer'),
    path('students_list/', students_list, name='students_list'),
    path('create_training/', create_training, name='create_training'),

]
