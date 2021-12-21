from django.urls import path
from . import views

app_name = "favfreelance"

urlpatterns = [
    path('favelist', views.favelist, name='favelist'),
]