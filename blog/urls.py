from django.urls import path
from . import views

urlpatterns = [
    path('', views.allBlogs, name='allBlogs'),
    path('<int:blogId>/', views.detail, name='detail')
]
