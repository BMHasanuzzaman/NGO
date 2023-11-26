from django.shortcuts import render, redirect
from django.urls import reverse

import stripe

stripe.api_key = "sk_test_51OGiOVHWO4uUX1gMZTTr7uWEX19ZEJnlTHO0r7QX1oEZR1YbCoVhehiUvrh9PiMsvO05Qm6eJFih5RYvgkuSVE7300siOpHYce"



# Create your views here.


def payment (request):
    return render(request, 'pay.html')

def charge(request):
    amount = 5
    if request.method == 'POST':
        print('data', request.POST)
    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
    amount = args
    return render(request, 'success.html',{'amount':amount})