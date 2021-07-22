from django.forms import ModelForm
from .models import Book, Customer, Order,Lend, Student

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class LendForm(ModelForm):
    class Meta:
        model = Lend
        fields = '__all__'


# class UpdateForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'