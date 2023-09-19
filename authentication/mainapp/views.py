from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import UserProfile
from .forms import UserRegistrationForm, UserProfileForm
# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():           
            new_user = user_form.save(commit=False)           
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return redirect('registration/register_done.html')
        
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
        return redirect('register_done', {'user_form': user_form, 'profile_form': profile_form})

def register_done(request):
    return render(request, 'registration/register_done.html')

