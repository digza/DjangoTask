from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import extras
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    dob = forms.DateField(widget=extras.SelectDateWidget(years=range(1901, 2003)), required=True)




    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'dob', 'password1', 'password2')
