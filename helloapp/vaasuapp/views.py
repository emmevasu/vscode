from django.http import HttpResponse

def home(request):
    return HttpResponse('<html><body><h1>Hello Vaasu, Welcome to Django!</h1></body></html>')