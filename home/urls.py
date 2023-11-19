from django.urls import path

from home import views

urlpatterns = [
    path('', views.indexpage, name='index'),
    path('about/', views.About, name='about')

]

