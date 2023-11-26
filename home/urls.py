from django.urls import path
from django.contrib import admin
from django.urls import path
from home import views
from .views import *



urlpatterns = [

    path('', views.indexpage, name='index'),
    path('about/', views.About, name='about'),
    path('gallery/', views.Gallery, name='gallery'),
    path('event/', views.Event, name='event'),
    path('donate/', views.Donate, name='donate'),
    path('contact/', views.Contact, name='contact'),
    path('blog/', views.Blog, name='blog'),
    path('causes/', views.Causes, name='causes'),
    path('blog/hurricane1.html/<int:pk>/', views.Hurricanes, name='hurricanes'),
    path('cause/causes1.html/<int:pk>/', views.Causer1, name='causer1'),


]

