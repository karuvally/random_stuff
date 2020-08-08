from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!, You are at the polls :)")


def easter_eggs(request):
    return(HttpResponse("There are no easter eggs here.")

