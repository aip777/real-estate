from django.urls import path


from . import views


urlpatterns = [
    path('', views.blogview, name='blogview'),
    path('<int:blog_id>/', views.blogid, name='blogid'),
]