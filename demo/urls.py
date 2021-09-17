"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('', include('business.urls')),
    # path('/index', include('business.urls')),
    # path('/about', include('business.urls')),
    # path('/contact', include('business.urls')),
    # path('/pricing', include('business.urls')),
    # path('/work', include('business.urls')),
    # path('/worksingle', include('business.urls')),
    path('admin/', admin.site.urls),
]
