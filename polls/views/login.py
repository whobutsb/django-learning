from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_login

def login_view(request):
    return render(request, 'polls/login.html')

def auth(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])

    if user is not None:
        messages.success(request, 'You logged in!')
        django_login(request, user)
        return redirect('polls:index')
    else:
        messages.error(request, 'Wrong username or password')
        return redirect('polls:login')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have logged out!')
    return redirect('polls:index')

