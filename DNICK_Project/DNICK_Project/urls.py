"""
URL configuration for DNICK_Project project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from Cigars.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pocetna/', pocetna, name= "pocetna"),
    path('cigars/', cigars, name= "cigars"),
    path('za_nas/', za_nas, name="za_nas"),
    path('kupuvac/', kupuvac, name="kupuvac"),
    path('prodavac/', prodavac, name="prodavac"),
    path('naracka/<int:id>', naracka, name="naracka"),
    path('najava/', najava, name="najava"),
    path('uspesna_pokupka/', uspesna_pokupka, name="uspesna_pokupka")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)