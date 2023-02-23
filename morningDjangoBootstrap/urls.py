"""morningDjangoBootstrap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base, name='base'),
    path('index/',views.index, name='index'),
    path('blog/',views.blog, name='blog'),
    path('cart/',views.cart, name='cart'),
    path('category/',views.category, name='category'),
    path('checkout/',views.checkout, name='checkout'),
    path('confirmation/',views.confirmation, name='confirmation'),
    path('contact/',views.contact, name='contact'),
    path('elements/',views.elements, name='elements'),
    path('login/',views.login, name='login'),
    path('single_blog/',views.single_blog, name='single_blog'),
    path('single_product/',views.single_product, name='single_product'),
    path('tracking/',views.tracking, name='tracking'),


]
