from django.urls import path

from . import views

app_name = "freelanceAdPage"

urlpatterns = [
    path('browse_page', views.browse_page, name='browse_page'),
    path('browse_fail', views.browse_fail, name='browse_fail'),
    path('freelance_ad_page', views.freelance_ad_page, name='freelance_ad_page'),
    path('create_ad_page', views.create_ad_page, name='create_ad_page'),
]