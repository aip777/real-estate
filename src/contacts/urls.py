from django.urls import path

from . import views

urlpatterns = [
  path('contact/', views.contact, name='contact'),
  path('contact/<int:pk>/', views.delete, name='delete'),
]