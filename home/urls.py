from django.urls import path

from home import views

urlpatterns = [
    path('', views.indexpage, name='index'),
    path('about/', views.About, name='about'),
    path('gallery/', views.Gallery, name='gallery'),
    path('event/', views.Event, name='event'),
    path('donate/', views.Donate, name='donate'),
    path('contact/', views.Contact, name='contact'),
    path('blog/', views.Blog, name='blog'),
    path('causes/', views.Causes, name='causes'),


]

