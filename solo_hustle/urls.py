"""
URL configuration for solo_hustle project.

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

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),  # Existing admin URL
#     path('home/', include('home.urls')),  # Existing home URL
#     path('', include('home.urls')),  # Add this line for the root path
#     path('', include('base.urls')),  # Add this line for the root path
# ]

from django.shortcuts import redirect
from django.urls import path, include

def redirect_to_login(request):
    return redirect("login")  # Redirects '/' to the login page

urlpatterns = [
    path("", redirect_to_login),  # Redirect root URL to login
    path("base/", include("base.urls")),  # Include authentication URLs
    path("home/", include("home.urls")),  # Include Home app URLs
]
