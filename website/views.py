from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()

    # check the see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('There was An Error Logging In - Please Try Again...'))
            return redirect('home')

    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # save the user
            form.save()
            # get the username and password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # authenticate user then login
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You have registered...'))
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, ('You Must Be Logged In To View That Page...'))
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        # Look up Records
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, ('Record Has Been Deleted...'))
        return redirect('home')
    else:
        messages.success(request, ('You Must Be Logged In To View That Page...'))
        return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, ('Record Has Been Added...'))
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, ('You Must Be Logged In To View That Page...'))
        return render(request, 'add_record.html', {})

def update_record(request, pk):
    if request.user.is_authenticated:
        # Look up Records
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)

        if form.is_valid():
            form.save()
            messages.success(request, ('Record Has Been Updated...'))
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, ('You Must Be Logged In To View That Page...'))
        return redirect('home')