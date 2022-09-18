from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# register view


def register(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("the form is valid")
            form.save()
            username = request.POST.get("username")
            password = request.POST.get("password1")
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("dashboard")
        print("the request mehtod is post for now.s")
    context = {"form": form}
    return render(request, "accounts/register.html", context)


# login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            print("there is no user")
            messages.error(request, "something went wrong")
    context = {}
    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")
