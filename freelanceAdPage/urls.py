from django.urls import path

from . import views

app_name = "freelanceAdPage"

urlpatterns = [
    path('browse_page', views.browse_page, name='browse_page'),
]