from django.urls import path

from payment import views

urlpatterns=[
    path('payment/',views.payment, name='payment'),
    path('charge/',views.charge,name="charge"),
    path('success/<str:args>/',views.successMsg, name="success")
]