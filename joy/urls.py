# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admissions/', views.admissions, name='admissions'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('academic_page/', views.academic_page, name='academic_page'),

]
