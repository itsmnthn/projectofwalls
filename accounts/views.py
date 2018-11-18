from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):

    if request.method == "POST":
        # User can sign up
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {"error": "Username already taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password'],
                    email=request.POST['email'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                )
                auth.login(request, user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return render(request, 'accounts/signup.html', {"error": "Both passwords must match"})
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        # Return sign up page
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == "POST":
        # User can sign up
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return render(request, 'accounts/login.html', {"error": "Username and password is incorrect"})
    else:
        # Return login page
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
