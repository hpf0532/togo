"""togo URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
# from django.conf.urls import handler404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class Error404(APIView):
    """404处理"""
    def get(self, request):
        response_data = {}
        response_data['detail'] = '404 Not found.'
        return Response(response_data, status.HTTP_404_NOT_FOUND)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    re_path('.*', Error404.as_view())
]

