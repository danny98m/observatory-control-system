from django.shortcuts import render


# Create your views here.
def home (request):
    return render(request, 'observatory_control/index.html')
