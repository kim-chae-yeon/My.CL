from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CategoryLog


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CategoryLogForm(forms.ModelForm):
    class Meta:
        model = CategoryLog
        fields = '__all__'
