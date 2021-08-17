from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default="user1.png",null= True, blank= True)

    def __str__(self):
        if self.name==None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default="user1.png",null= True, blank= True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    CATEGORY=(
        ('Novel','Novel'),
        ('Literature','Literature'),
    )
    STATUS=(
        ('Pending','Pending'),
        ('Returned','Returned'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('out of delivery','out of delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.book.name


class Lend(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Returned','Returned'),
    )
    student = models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.book.name
