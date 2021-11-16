"""
路由子表，所有关于app bigdata的路由全部由这个文件负责
"""
from django.urls import path
from . import views

app_name = 'bigdata'
urlpatterns = [
    path('', views.brokenline, name='index'),
    # path('orders/', views.listorders),
]