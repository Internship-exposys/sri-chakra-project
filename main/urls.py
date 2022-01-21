from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main-index'),
    path('contactus/index', views.index, name='main-index'),
    path('about/', views.about, name='main-about'),
    path('kriston/', views.kriston, name='main-kriston'),
    path('srichakra/', views.srichakra, name='main-srichakra'),
    path('suryaIntech/', views.suryaIntech, name='main-suryaIntech'),
    path('products/', views.products, name='main-products'),
    path('products/kriston/', views.products_kriston, name='main-kriston'),
    path('products/srichakra/', views.products_srichakra, name='main-srichakra'),
    path('products/suryaIntech/', views.products_suryaIntech, name='main-suryaIntech'),


]
