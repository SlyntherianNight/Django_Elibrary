from django import contrib
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
# create your views here 
from .models import *
from .forms import BookForm, CustomerForm, OrderForm,LendForm, StudentForm,CreateUserForm
from .filters import OrderFilter,LendFilter,BookFilter
from .decorators import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# for flash message
from django.contrib import messages

# Create your views functions here.
# user-Arun 
# password - ArunDhumal 
# user2-Ranjana 
# email-ranjana@gmail.com 
# password - RanDhumal 

def home(request):
    return render(request,'home.html')

def api_base(request,pk):
    customers = Customer.objects.get(id= pk)
    print(customers)
    orders = customers.order_set.all()
    books = Book.objects.all()
    total_books = books.count()
    totalorders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    returned = orders.filter(status='Returned').count()
    # for adding search filter on customer product table 
    myFilter = OrderFilter(request.POST,queryset=orders)
    orders = myFilter.qs

    context = {'customers':customers,'orders':orders,'books': books,'total_books':total_books,'totalorders':totalorders,'delivered':delivered,'returned':returned,'myFilter':myFilter}
    return render(request,'api_base.html',context)

def customer_registerPage(request):
    form1 = CreateUserForm()
    if request.method=='POST':
        form1 = CreateUserForm(request.POST)
        print(form1)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + username)

            return redirect('loginPage')        

    context = {}   
    context.update({'form1':form1}) 
    return render(request, 'cus_registerPage.html',context)

def student_registerPage(request):
    form1 = CreateUserForm()
    if request.method=='POST':
        form1 = CreateUserForm(request.POST)
        if form1.is_valid()==True:
            form1.save()
            return redirect('loginPage')
            
        elif form1.is_valid()==False:
            user = form1.save()
            username = form1.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + username)

            return redirect('login')

    context = {'form1':form1}    
    return render(request, 'stud_registerPage.html',context)

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username , password = password)
            
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
                
        else:
            messages.warning(request,'Username or Password is incorrect')
    context={}
    return render(request, 'login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='home')
@allowed_users(allowed_roles=['admin','customer','student'])
def userPage(request,pk):
    orders = request.user.customer.order_set.all()
    print('Orders:',orders)
    customers = Customer.objects.get(id= pk)
    orders = customers.order_set.all()
    books = Book.objects.all()
    total_books = books.count()
    totalorders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    returned = orders.filter(status='Returned').count()
    # for adding search filter on customer product table 
    myFilter = OrderFilter(request.POST,queryset=orders)
    orders = myFilter.qs

    context={'orders':orders,'customers':customers,'orders':orders,'books': books,'total_books':total_books,'totalorders':totalorders,'delivered':delivered,'returned':returned,'myFilter':myFilter}
    return render(request, 'customers.html',context)


@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
def admin_dashboard(request):
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
    return render(request,'admin_dashboard.html',context)

@login_required(login_url='home')
@allowed_users(allowed_roles=['admin','customer','student'])
def dashboard(request):
    customers = Customer.objects.all()
    students = Student.objects.all()
    orders = Order.objects.all()
    lends = Lend.objects.all()
    cou = lends.count()
    userkon = request.user
    books = Book.objects.all()
    # for adding search filter on customer product table 
    myFilter = BookFilter(request.GET, queryset= books)
    books = myFilter.qs
    total_books = books.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()

    context = {'customers':customers,'students':students,'userkon':userkon,'lends':lends,'cou':cou,'orders':orders,'books': books,'total_books':total_books,'total_orders':total_orders,'delivered':delivered,'pending':pending,'myFilter':myFilter}
    return render(request,'dashboard.html',context)

@login_required(login_url='customers')
def customers(request,pk):
    customers = Customer.objects.get(id= pk)
    orders = customers.order_set.all()
    books = Book.objects.all()
    total_books = books.count()
    totalorders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    returned = orders.filter(status='Returned').count()
    # for adding search filter on customer product table 
    myFilter = OrderFilter(request.POST,queryset=orders)
    orders = myFilter.qs

    context = {'customers':customers,'orders':orders,'books': books,'total_books':total_books,'totalorders':totalorders,'delivered':delivered,'returned':returned,'myFilter':myFilter}
    return render(request,'customers.html',context)

@login_required(login_url='home')
def students(request,pk):
    students = Student.objects.get(id= pk)
    lends = students.lend_set.all()
    books = Book.objects.all()
    total_books = books.count()
    totallends = lends.count()
    delivered = lends.filter(status='Delivered').count()
    returned = lends.filter(status='Returned').count()
    # for adding search filter on customer product table 
    myFilter = LendFilter(request.POST, queryset= lends)
    lends = myFilter.qs

    context = {'students':students,'lends':lends,'books': books,'total_books':total_books,'totallends':totallends,'delivered':delivered,'returned':returned,'myFilter':myFilter}
    return render(request,'students.html',context)

@login_required(login_url='home')
def books(request):
    books = Book.objects.all()
    customers = Customer.objects.all()
    # for adding search filter on customer product table 
    myFilter = BookFilter(request.GET, queryset= books)
    books = myFilter.qs

    context ={'books': books,'myFilter':myFilter,'customers':customers}
    return render(request,'books.html',context)

@login_required(login_url='home')
def reports(request):
    return render(request,'reports.html')

@login_required(login_url='home')
def about(request):
    return render(request,'about.html')

@login_required(login_url='home')
@allowed_users(allowed_roles=['admin','customer','student'])
def settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'settings.html',context)



@login_required(login_url= 'home')
def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context={'form':form}
    return render(request,'students_form.html', context)

@login_required(login_url= 'home')
def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context={'form':form}
    return render(request,'customers_form.html', context)

@login_required(login_url='home')
def createOrder(request, pk):
    order = Order.objects.get(id=pk)
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/elibrary/customers/'+pk)
    context={'form':form,'order':order,'customer':customer}
    return render(request,'orders_form.html', context)


@login_required(login_url='home')
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/elibrary/customers/'+ pk)
    context={'form':form}
    return render(request,'orders_form.html', context)

@login_required(login_url='home')
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/customers/'+pk)
    context={'item':order}
    return render(request,'delete.html', context)

@login_required(login_url='home')
def createLend(request, pk):
    student = Student.objects.get(id=pk)
    form = LendForm(initial={'student':student})
    if request.method == 'POST':
        form = LendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/elibrary/students/'+ pk)
    context={'form':form,'student':student}
    return render(request,'lends_form.html', context)

@login_required(login_url='home')
def updateLend(request,pk):
    lend = Lend.objects.get(id=pk)
    form = LendForm(initial={'lend':lend})
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = LendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/elibrary/students/'+ pk)
    context={'form':form}
    return render(request,'lends_form.html', context)

@login_required(login_url='home')
def deleteLend(request,pk):
    lend = Lend.objects.get(id=pk)
    if request.method == 'POST':
        lend.delete()
        return redirect('/elibrary/students/'+ pk)
    context={'item':lend}
    return render(request,'delete.html', context)

@login_required(login_url='home')
def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/elibrary/books')
    context={'form':form}
    return render(request,'books_form.html', context)

@login_required(login_url='home')
def updateBook(request,pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        # print('Printing Post : ', request.POST)
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/elibrary/books')
    context={'form':form}
    return render(request,'books_form.html', context)

@login_required(login_url='home')
def deleteBook(request,pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('/elibrary/books')
    context={'item':book}
    return render(request,'delete.html', context)
    