from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello suka")


def details(request):
    return HttpResponse("You are looking at details, suka")

def graphic(request):
    return HttpResponse("You are looking at graphic, suka")