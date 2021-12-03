from django.urls import path
from .views import review

urlpatterns = [
    path('', review, name='review'),
]