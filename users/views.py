from django.shortcuts import render, redirect
from .models import User, UserStats


def user_main(request):
    user = User.objects.filter(user_id=1).first()
    return render(request, 'users/users_main.html', {'user': user})


def user_stats(request):
    user_stats = UserStats.objects.filter(user_id=1).first()
    return render(request, 'users/user_stats.html', {'user_stats': user_stats})




