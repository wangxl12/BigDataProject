"""
路由子表，所有关于app bigdata的路由全部由这个文件负责
"""
from django.urls import path
from . import views

app_name = 'bigdata'
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('buy_most_user/', views.buy_most_user, name='buy_most_user'),
    path('cart_most_user/', views.cart_most_user, name='cart_most_user'),
    path('fav_most_user/', views.fav_most_user, name='fav_most_user'),
    path('productsID_statisctis/', views.productsID_statisctis, name='productsID_statisctis'),
    path('productsClassID_statistics/', views.productsClassID_statistics, name='productsClassID_statistics'),
    path('single_user_behavior_statistics/', views.single_user_behavior_statistics, name='single_user_behavior_statistics'),
    path('cluster/', views.cluster, name='cluster'),
    # path('demomap/', views.buy_most_user, name='buy_most_user'),
]