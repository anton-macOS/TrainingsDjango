from django.urls import path

from .views import welcome_user, user_stats

urlpatterns = [
    path('', welcome_user, name='welcome_user'),
    path('user-stats/', user_stats, name='user_stats')

]