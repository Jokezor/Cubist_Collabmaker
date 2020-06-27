"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include
# changed from 2 to 3
from Landing_page import urls as urls_landing_page
from Landing_page.views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Swagger Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    re_path(r'^', include(urls_landing_page)),
    #path for Swagger
    path('swagger/',schema_view),
    path('accounts/',include('rest_framework.urls')),
    
    ] 
    
