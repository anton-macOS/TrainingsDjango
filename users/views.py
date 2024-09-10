from django.http import HttpResponse


def welcome_user(request):
    return HttpResponse('<h1>This is users page!</h1>')

def user_stats(request):
    return  HttpResponse('<h1>This is user stats page</h1>')
