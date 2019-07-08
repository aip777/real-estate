from django.urls import path


from . import views
from .views import BookListView, UploadBookView


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('upload/', views.upload, name='upload'),
    # path('books/', views.book_list, name='book_list'),
    # path('books/upload/', views.upload_book, name='upload_book'),
    #
    # path('books/<int:pk>/', views.delete_book, name='delete_book'),

    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    path('class/books/<int:pk>/', views.class_delete_book, name='class_delete_book'),



]