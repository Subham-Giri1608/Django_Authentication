from django import forms
from django.contrib.auth.models import User 
from .models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email', )
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile  
        fields = ('phone_number', 'current_city', 'school', 'college')    
