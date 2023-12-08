from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if User.objects.filter(username=username).exists():
            messages.warning(request, "This username already exists!")
            return redirect("users:register")

        if password != password_confirm:
            messages.warning(request, "Passwords don't match")
            return redirect("users:register")

        User.objects.create_user(
            username=username,
            password=password,
        )

        messages.success(request, "Successfully registered, try logging in now!")
        return redirect("users:login")


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Successfully logged in")

            return redirect("home")
        
        messages.warning(request, "incorrect username or/and password")
        return redirect("users:login")