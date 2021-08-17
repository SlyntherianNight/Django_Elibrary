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

from django.conf.urls import url
from django.urls import include, path
from . import views
# email authentication to reset password 
# https://docs.djangoproject.com/en/3.2/topics/auth/default/ 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name ='home'),
    path('api_base/<str:pk>/', views.api_base, name ='api_base'),
    path('customer_register/', views.customer_registerPage, name ='customer_registerPage'),
    path('student_register/', views.student_registerPage, name ='student_registerPage'),
    path('login/', views.loginPage, name ='loginPage'),
    path('logout/', views.logoutuser, name ='logoutuser'),
    path('user/<str:pk>/', views.customers, name ='userPage'),
    path('admin_dashboard/', views.admin_dashboard, name ='admin_dashboard'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('students/<str:pk>/', views.students, name ='students'),
    path('customers/<str:pk>/', views.customers, name ='customers'),
    path('books/', views.books, name ='books'),
    path('reports/', views.reports, name ='reports'),
    path('about/', views.about, name ='about'),
    path('settings/', views.settings, name ='settings'),

    
    # admin control- to create,update & delete students & customers
    path('create_student/', views.createStudent, name ='create_student'),
    path('create_customer/', views.createCustomer, name ='create_customer'),

    # to create,update & delete ordered placed by customer
    path('create_order/<str:pk>/', views.createOrder, name ='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name ='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name ='delete_order'),

    # to create,update & delete the book lend by a student
    path('create_lend/<str:pk>/', views.createLend, name ='create_lend'),
    path('update_lend/<str:pk>/', views.updateLend, name ='update_lend'),
    path('delete_lend/<str:pk>/', views.deleteLend, name ='delete_lend'),

    # to create,update & delete the book 
    path('create_book/', views.createBook, name ='create_book'),
    path('update_book/<str:pk>/', views.updateBook, name ='update_book'),
    path('delete_book/<str:pk>/', views.deleteBook, name ='delete_book'),
    
    # ''' for password reset email verification
    # 1 - Submit email form           
    # 2 - Email sent success message 
    # 3 - Link to password rest form in email
    # 4 - Password successfully changed message 
    # '''

    path('password-reset/', auth_views.PasswordResetView.as_view() ,name= "reset_password"),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view() ,name= "password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view() ,name= "password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view() ,name= "password_reset_complete"),
    




    # path('password-reset-done/', auth_views.PasswordResetDoneView.as_view() ,name= "password_reset_done"), 
    # # ''' it renders success message & let us know that password is sent, notify user to check there mail'''
    # path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view() ,name= "password_reset_confirm"),
    # # '''this sends link to user through email entered by which user can submit form , <uidb64>--users id encoded in base 64, <token> -->to check password is valid'''
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view() ,name= "password_reset_complete"),

]
