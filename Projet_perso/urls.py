"""
URL configuration for Projet_perso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from HC_site import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('HC_site.urls')),
    path('contact_envoyer/', views.page_detail, name='contact_message'),
    path('merci/', lambda request: render(request, 'merci.html'), name='merci'),

    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    





