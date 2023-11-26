from django.shortcuts import render, get_object_or_404
from .models import *





# Create your views here.
def indexpage(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Gallery(request):
    pics = Image.objects.all()
    return render(request, 'gallery.html', {"pics": pics})

def Causes(request):
    category = Causers.objects.all()
    context={
        'category':category,
    }
    return render(request, 'causes.html',context)


def Contact(request):
    return render(request, 'contact.html')

def Event(request):
    return render(request, 'event.html')

def Donate(request):
    return render(request, 'donate.html')

def Blog(request):
    category = Hurricane.objects.all()
    context={
        'category':category,
    }
    return render(request, 'blog.html', context)


def Hurricanes(request,pk):
    post=Hurricane.objects.get(id=pk)
    context={
        'post':post,
    }
    # context = get_object_or_404(Hurricane, pk=id)
    return render(request,'hurricane1.html',context)

def Causer1(request,pk):
    post=Causers.objects.get(id=pk)
    context={
        'post':post,
    }
    # context = get_object_or_404(Hurricane, pk=id)
    return render(request,'causes1.html',context)
