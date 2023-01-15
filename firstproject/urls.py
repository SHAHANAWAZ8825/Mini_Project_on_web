"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include
from django.urls import re_path as url
#from exam import views as views_exam
#from testapp import views as views_testapp

urlpatterns = [
    url('testapp',include('testapp.urls')),
    url('exam',include('exam.urls')),
    url('BRMapp/',include('BRMapp.urls')),
   # path('exam/',views_exam.showExam),
   # path('result/',views_exam.showResult),
   # path('about/',views_testapp.about),
   # path('contact',views_testapp.showContact),
   # url('^$',views_testapp.greeting),
    path('admin/', admin.site.urls),
]
