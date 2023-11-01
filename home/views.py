from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')