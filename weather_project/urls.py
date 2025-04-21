"""
URL configuration for weather_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/weather/', include('weather.urls')),  # make sure this line exists
]


from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the UK Weather API</h1><p>Visit <code>/api/weather/data/</code> to see weather data.</p>")

urlpatterns = [
    path('', home),  # 👈 this handles the root path
    path('admin/', admin.site.urls),
    path('api/weather/', include('weather.urls')),
]


