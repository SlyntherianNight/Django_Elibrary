# I created this urls.py file 

from django.urls import include, path
from . import views

from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name ='covicare_home'),
    path('chat/', views.chat, name ='covicare_chat'),
    path('covicare_about/', views.covicare_about, name ='covicare_about'),
    path('contact/', views.contact, name ='covicare_contact'),
]

