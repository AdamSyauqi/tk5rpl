from django.urls import path

from . import views

urlpatterns = [
    path('browse_page', views.browse_page, name='browse_page'),
]