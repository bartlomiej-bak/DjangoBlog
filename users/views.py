from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


# Decorator which prevents opening profile page for not logged users,
@login_required()
def profile(request):
    return render(request, 'users/profile.html')
