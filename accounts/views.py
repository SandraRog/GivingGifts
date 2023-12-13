from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View

from .forms import LoginForm


class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatyczne zalogowanie użytkownika po rejestracji
            return redirect('login')  # Tutaj podaj nazwę widoku, na który chcesz przekierować użytkownika po
            # rejestracji
        return render(request, 'register.html', {'form': form, 'errors': form.errors})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error('password', 'Błędne hasło.')



        return render(request, 'login.html', {'form': form})

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('landing_page')