"""
URL configuration for busbooking project.

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
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buses', include('booking.urls')),
    path('accounts/', include('accounts.urls')),
    path('', RedirectView.as_view(url='/accounts/home/', permanent=False)),
    
    # path('accounts/home/edit_profile', RedirectView.as_view(url='accounts/edit_profile/', permanent=False)),
    # path('edit_profile', RedirectView.as_view(url='accounts/edit_profile/', permanent=False)),
    # path('busesfiltered_bookings/edit_profile', RedirectView.as_view(url='accounts/edit_profile/', permanent=False)), 
]

# accounts/home/edit_profile
# edit_profile
# busesfiltered_bookings/edit_profile
