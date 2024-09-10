from django.http import HttpResponse

def exercises(request):
    return HttpResponse('<h1>This is exercises page</h1>')
