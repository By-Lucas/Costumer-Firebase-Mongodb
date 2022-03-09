from django.shortcuts import render

# Create your views here.

def index(request):
    data = {}
    data['usuario'] =  request.user
    return render(request, "index.html", data)
    