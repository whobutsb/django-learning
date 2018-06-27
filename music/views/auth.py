from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request, 'auth/index.html')

def authenticate(request):
    user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        messages.success(request, 'You logged in!')
        auth.login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'Wrong username or password')
        return redirect('auth.index')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have logged out!')
    return redirect('auth.index')


