"""
URL configuration for Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import home
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path("gallery.html", views.Gallery),
    path("causes.html", views.Causes),
    path("contact.html", views.Contact),
    path("donate.html", views.Donate),
    path("blog.html", views.Blog),
    path("about.html", views.About),
    path("event.html", views.Event),
    path("index.html", views.indexpage)


]
