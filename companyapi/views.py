from django.http import HttpResponse


def about(request):
    print("Testing")
    return HttpResponse ("Hello")