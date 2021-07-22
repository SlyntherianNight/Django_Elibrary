from django.contrib import admin

# Register your models here.
from .models import Book, Customer, Lend, Order, Student, Tag

admin.site.register(Customer)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Lend)