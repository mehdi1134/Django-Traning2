from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
# Create your views here.

def user_register(request):
    if request.method == "POST":
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
          cd=form.cleaned_data
          User.objects.create_user(cd["username"], cd["email"], cd["password"])
          messages.success(request , "user is registered successfully")
          return redirect("home")

    else:
        form= UserRegistrationForm()
        return render(request, 'user_register.html', {"form":form})
    
  

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd["username"],
                password=cd["password"]
            )

            if user is not None:
                login(request, user)
                messages.success(request, f"{ user.username} Logged in successfully!! ...")
                return redirect("home")
            
            messages.error(request, "Username or password is wrong")

    else:
        form = UserLoginForm()

    return render(request, "user_login.html", {"form": form})

def user_logout(request):
       logout(request)
       messages.success(request, "Logged out!")
       return redirect('home')