from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Gallery(request):
    return render(request, 'gallery.html')

def Causes(request):
    return render(request, 'causes.html')

def Contact(request):
    return render(request, 'contact.html')

def Event(request):
    return render(request, 'event.html')

def Donate(request):
    return render(request, 'donate.html')

def Blog(request):
    return render(request, 'blog.html')