from django.urls import path
from Blog import views

urlpatterns = [
    path('',views.blog_index, name='blog_index'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]