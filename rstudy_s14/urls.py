"""rstudy_s14 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app01 import views
from django.urls.conf import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home', views.home),
    path('upload/', views.upload),
    path('cbv/', views.Cbv.as_view()),
    path('list/', views.List.as_view(), name="llist"),
    # re_path(r'detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.Detail.as_view())
    re_path(r'detail-(?P<nid>\d+).html', views.Detail.as_view()),
    path('cmdb/', include("cmdb.urls")),
    path('monitor/', include("monitor.urls"))
]
