from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after sign-up
            return redirect("home")  # Redirect to Home after signup
    else:
        form = UserCreationForm()
    return render(request, "base/signup.html", {"form": form})
