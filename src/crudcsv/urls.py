
from django.urls import path


from . import views


urlpatterns = [

    # path('fileupload/', views.fileupload, name='fileupload'),
    path('upload/csv/', views.upload_csv, name='upload_csv'),
    path('upload/csv/create/', views.CreateCsv.as_view(), name='create'),
    path('upload/csv/edit/<int:id>/', views.edit, name='edit'),
    path('upload/csv/update/<int:id>/', views.update, name='update'),
    path('upload/csv/delete/<int:id>/', views.delete, name='delete'),
    # path('upload/', views.upload, name='upload'),
    # path('books/upload/', views.upload_book, name='upload_book'),


]