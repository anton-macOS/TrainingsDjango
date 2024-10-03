from django.urls import path

from .views import user_main, user_stats
app_name = 'users'

urlpatterns = [
    path('', user_main, name='user_main'),
    path('user_stats/', user_stats, name='user_stats')

]
