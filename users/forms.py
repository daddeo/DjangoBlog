from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # nested namespace for configurations
    class Meta:
        model = User # the model effected
        fields = ["username", "email", "password1", "password2"] # fields on form and in what order

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    # nested namespace for configurations
    class Meta:
        model = User # the model effected
        fields = ["username", "email"] # fields on form and in what order

class ProfileUpdateForm(forms.ModelForm):
    # nested namespace for configurations
    class Meta:
        model = Profile # the model effected
        fields = ["image"] # fields on form and in what order
