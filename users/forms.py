from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'логин'}), label='Логин')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'пароль'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'повторите пароль'}), label='Подтверждение пароля')

    field_order = ["user_name", "password1", "password2"]

    class Meta:
        model = User
        fields = {'user_name', 'password1', 'password2'}

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)






