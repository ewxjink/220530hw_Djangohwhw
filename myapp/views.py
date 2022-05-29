from django.shortcuts import render

def introduce(request):
    return render(request, 'introduce.html')
# Create your views here.
