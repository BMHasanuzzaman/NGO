from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings
# from backend.settings import EMAIL_HOST_USER




# def send_email(request):
#     # saveEnquiry()
#     return redirect('/')

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
    # if request.method == "POST":
    #     name=request.POST['name']
    #     email=request.POST['email']
    #     subject=request.POST['subject']
    #     message=request.POST['message']
    #     return render(request, 'contact.html',{'name','email','subject','message'})
    # else:
        return render(request,'contact.html')

def saveEnquiry(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        en=contactInfo(name=name,email=email,subject=subject,message=message)
        en.save()

        email_message = f"Email: {email}\nSubject: {subject}\nMessage: {message}"

        # send an email
        send_mail(
            name,
            email_message,
            'km.fazla@northsouth.edu',
            ['k.m.fazlarabby51@gmail.com'],
            # fail_silently=False,
        )


    return render(request,"contact.html")

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
