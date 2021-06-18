from django.urls import path
from .views import upload_csv, CreateCsv, edit, update, delete
urlpatterns = [

    # path('fileupload/', views.fileupload, name='fileupload'),
    path('upload/csv/', upload_csv, name='upload_csv'),
    path('upload/csv/create/', CreateCsv.as_view(), name='create'),
    path('upload/csv/edit/<int:id>/', edit, name='edit'),
    path('upload/csv/update/<int:id>/', update, name='update'),
    path('upload/csv/delete/<int:id>/', delete, name='delete'),
    # path('upload/', views.upload, name='upload'),
    # path('books/upload/', views.upload_book, name='upload_book'),


]