from django.shortcuts import render

def introduce(request):
    return render(request, 'introduce.html')

def image(request):
    return render(request, 'image.html')

def Charlie(request):
    return render(request, 'Charlie.html')

def prac(request):
    return render(request, 'prac.html')

def test(request):
    return render(request, 'test.html')
# Create your views here.
