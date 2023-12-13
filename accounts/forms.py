from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import MyUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Imię'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Podaj hasło'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'})
    )

    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Hasła nie są zgodne. Proszę wprowadzić te same hasła.")

        email = cleaned_data.get("email")
        if MyUser.objects.filter(email=email).exists():
            raise ValidationError("Istnieje już użytkownik z tą wartością pola Email.")

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        required=True,
        error_messages = {'required': 'To pole jest wymagane.', 'invalid': 'Podaj prawidłowy adres email.'}
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}),
        required=True,
        error_messages={'required': 'To pole jest wymagane.'}
    )
