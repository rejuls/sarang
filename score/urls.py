

from django.contrib import admin
from django.urls import path, include
from score import views
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [

    path('', views.Match_list, name='Match'),
    path('results/', views.Results_list, name='Result'),

]
