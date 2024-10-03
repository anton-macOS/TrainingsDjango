from django.shortcuts import render
from .models import Supplements


def supplements(request):
    user_supplements = Supplements.objects.filter(user_id=1).first()
    return render(request, 'users/user_supplements.html',
                  {'user_supplements': user_supplements})
