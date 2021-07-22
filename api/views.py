from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

# create your views here 
from .models import *
from .forms import BookForm, CustomerForm, OrderForm,LendForm, StudentForm
from .filters import OrderFilter,LendFilter,BookFilter
from django.contrib.auth.forms import UserCreationForm

# Create your views functions here.
def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'register.html',context)

def loginPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'login.html',context)

def index(request):
    customers = Customer.objects.all()
    students = Student.objects.all()
    orders = Order.objects.all()
    lends = Lend.objects.all()
    cou = lends.count()
    books = Book.objects.all()
    total_books = books.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()

    context = {'customers':customers,'students':students,'lends':lends,'cou':cou,'orders':orders,'books': books,'total_books':total_books,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'dashboard.html',context)

def customers(request,pk):
    customers = Customer.objects.get(id= pk)
    orders = customers.order_set.all()
    books = Book.objects.all()
    total_books = books.count()
    totalorders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    returned = orders.filter(status='Returned').count()
    # for adding search filter on customer product table 
    myFilter = OrderFilter(request.GET, queryset= orders)
    orders = myFilter.qs

    context = {'customers':customers,'orders':orders,'books': books,'total_books':total_books,'totalorders':totalorders,'delivered':delivered,'returned':returned,'myFilter':myFilter}
    return render(request,'customers.html',context)

def students(request,pk):
    students = Student.objects.get(id= pk)
    lends = students.lend_set.all()
    books = Book.objects.all()
    total_books = books.count()
    totallends = lends.count()
    delivered = lends.filter(status='Delivered').count()
    returned = lends.filter(status='Returned').count()
    # for adding search filter on customer product table 
    myFilter = LendFilter(request.GET, queryset= lends)
    lends = myFilter.qs

    context = {'students':students,'lends':lends,'books': books,'total_books':total_books,'totallends':totallends,'delivered':delivered,'returned':returned,'myFilter':myFilter}
    return render(request,'students.html',context)

def books(request):
    books = Book.objects.all()
    # for adding search filter on customer product table 
    myFilter = BookFilter(request.GET, queryset= books)
    books = myFilter.qs

    context ={'books': books,'myFilter':myFilter}
    return render(request,'books.html',context)

def reports(request):
    return render(request,'reports.html')

def about(request):
    return render(request,'about.html')





def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'students_form.html', context)

def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'customers_form.html', context)


def createOrder(request, pk):
    # OrderFormSet = inlineformset_factory(Customer, Order, fields={'book','status'})
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customers/'+pk)
    context={'form':form}
    return render(request,'orders_form.html', context)

def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/customers/'+ pk)
    context={'form':form}
    return render(request,'orders_form.html', context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/customers/'+pk)
    context={'item':order}
    return render(request,'delete.html', context)

def createLend(request, pk):
    student = Student.objects.get(id=pk)
    form = LendForm(initial={'student':student})
    if request.method == 'POST':
        form = LendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/'+ pk)
    context={'form':form,'student':student}
    return render(request,'lends_form.html', context)

def updateLend(request,pk):
    lend = Lend.objects.get(id=pk)
    form = LendForm(instance=lend)
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = LendForm(request.POST, instance=lend)
        if form.is_valid():
            form.save()
            return redirect('/students/'+ pk)
    context={'form':form}
    return render(request,'lends_form.html', context)

def deleteLend(request,pk):
    lend = Lend.objects.get(id=pk)
    if request.method == 'POST':
        lend.delete()
        return redirect('/students/'+ pk)
    context={'item':lend}
    return render(request,'delete.html', context)

def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')
    context={'form':form}
    return render(request,'books_form.html', context)

def updateBook(request,pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')
    context={'form':form}
    return render(request,'books_form.html', context)

def deleteBook(request,pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('/books')
    context={'item':book}
    return render(request,'delete.html', context)
    