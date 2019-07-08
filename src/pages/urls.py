from django.urls import path


from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('contactus/', views.contactus, name = 'contactus'),
    path('bootstrap/', views.bootstrap, name = 'bootstrap'),

    # path('upload/', views.upload, name='upload'),
    # path('books/upload/', views.upload_book, name='upload_book'),

]