from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username  # Use the saved user instance
            messages.success(request, f'Account created for {username} is successfull!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')