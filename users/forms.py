from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # nested namespace for configurations
    class Meta:
        model = User # the model effected
        fields = ["username", "email", "password1", "password2"] # fields on form and in what order

