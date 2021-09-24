# user defined views.py file 
from django.shortcuts import render, redirect

def main_home(request):
    return render(request,'main_home.html')

def resume(request):
    return render(request,'resume.html')

def portfolio(request):
    return render(request,'portfolio.html')

def abhi_contact(request):
    return render(request,'abhi_contact.html')