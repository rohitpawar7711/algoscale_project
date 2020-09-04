from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import SignupForm



# Create your views here.

@login_required
def homepage_view(request):
    return render(request, "LoginApp/home.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signup')
        else:
            return redirect('signup')

    return render(request, "LoginApp/login.html")

def logout_view(request):
    logout(request)
    return render(request, 'LoginApp/logout.html')


def signup_view(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'LoginApp/signup.html', {'form': form})
