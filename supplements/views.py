from django.http import HttpResponse

def supplements(request):
    return HttpResponse('<h1>This is supplements page</h1>')
