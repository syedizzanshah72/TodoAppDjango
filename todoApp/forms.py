from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models
from .models import TodoModel

class UserRegistrationform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
     model = User
     fields = ('username','email','password1','password2')

    widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'style': 'margin-bottom: 10px;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'style': 'margin-bottom: 10px;'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'margin-bottom: 10px;'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password',
            'style': 'margin-bottom: 10px;'
        })

class todoForm(forms.ModelForm):
    
    class Meta:
        model = TodoModel
        fields = ("tasktitle","description","due_date","priority")
        widgets = {
            'tasktitle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Task title...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description...'
            }),
            'due_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
