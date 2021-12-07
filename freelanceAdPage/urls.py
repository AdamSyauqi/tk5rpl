from django.urls import path

from . import views

app_name = "freelanceAdPage"

urlpatterns = [
    path('browse_page', views.browse_page, name='browse_page'),
    path('freelance_ad_page/<str:pk>/', views.freelance_ad_page, name='freelance_ad_page'),
    path('create_ad_page', views.create_ad_page, name='create_ad_page'),
    path('created_freelance_ad_page_list', views.created_freelance_ad_page_list, name="created_freelance_ad_page_list"),
    path('update_ad_page/<str:pk>/', views.update_ad_page, name='update_ad_page'),
    path('delete_ad_page/<str:pk>/', views.delete_ad_page, name='delete_ad_page'),
]