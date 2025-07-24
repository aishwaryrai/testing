from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateField(input_formats=[
        '%Y-%m-%d',  # 2025-07-23
        '%d-%m-%Y',  # 23-07-2025
        '%d/%m/%Y',  # 23/07/2025
    ])
    time = forms.TimeField(input_formats=[
        '%H:%M',     # 14:30
        '%I:%M %p',  # 02:30 PM
    ])

    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location']   


# User registration and login forms
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass
