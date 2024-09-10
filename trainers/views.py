from django.http import HttpResponse

def welcome_trainer(request):
    return HttpResponse('<h1>This is trainers page!</h1>')

