from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "post":
        form = UserCreationForm(request.post)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect("survey_design/")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})
