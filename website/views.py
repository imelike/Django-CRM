from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
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
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})