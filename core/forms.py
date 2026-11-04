from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl bg-white outline-none border-0"
class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            "placeholder":"Your username",
            "class": INPUT_CLASSES
    })) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            "placeholder":"Your password",
            "class":INPUT_CLASSES
        })) 

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            return username.lower()
        return username  



class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Your username",
        "class": INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder":"Your email",
        "class":INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Your password",
        "class":INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm your password",
        "class":INPUT_CLASSES
    }))
    