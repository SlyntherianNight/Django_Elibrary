"""Elibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# akshay's password is akdhumal652@

from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('register/', views.registerPage, name ='registerPage'),
    path('students/<str:pk>/', views.students, name ='students'),
    path('customers/<str:pk>/', views.customers, name ='customers'),
    path('books/', views.books, name ='books'),
    path('reports/', views.reports, name ='reports'),
    path('about/', views.about, name ='about'),
    
    # for dashboard student create option btn 
    path('create_student/', views.createStudent, name ='create_student'),
    path('create_customer/', views.createCustomer, name ='create_customer'),

    path('create_order/<str:pk>/', views.createOrder, name ='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name ='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name ='delete_order'),

    path('create_lend/<str:pk>/', views.createLend, name ='create_lend'),
    path('update_lend/<str:pk>/', views.updateLend, name ='update_lend'),
    path('delete_lend/<str:pk>/', views.deleteLend, name ='delete_lend'),

    path('create_book/', views.createBook, name ='create_book'),
    path('update_book/<str:pk>/', views.updateBook, name ='update_book'),
    path('delete_book/<str:pk>/', views.deleteBook, name ='delete_book'),
]
