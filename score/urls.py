

from django.contrib import admin
from django.urls import path, include
from score import views
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [

    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
