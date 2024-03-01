from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("Form Valid")
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('survey-home')
        else:
            print("Form Not Valid")
    else:
        form = UserRegisterForm()
        print("Skipped")
    return render(request, 'users/register.html', {'form': form})
