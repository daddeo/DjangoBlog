from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
#from request import request

# messages statuses can be:
# messages.[debug, info, success, warning, error]

# Create your views here.
def register(request):
    if request.method == "POST":
        # create a new form with the data posted
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # saves the user
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}.")
            return redirect("blog-home")
    else:
        form = UserRegistrationForm()
    return render(request, "users/register.html", {"form": form})