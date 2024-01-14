from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from . models import UserProfile


class UserForm(UserCreationForm):
    '''
    form that uses built-in usercreationform to handel user creation
    '''
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your Last Name'}))
    username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Email...'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'*Password...', 'class': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'*Confirm Password...', 'class': 'password'}))

    #reCAPTCHA token
    token = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class AuthForm(AuthenticationForm):
    '''
    form that uses built in authenticationform to handel user auth
    '''
    username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Email...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '*Password...','class': 'password'}))

    class Meta():
        model = User
        fields = ('username', 'password')



class UserProfileForm(forms.ModelForm):
    '''
    basic model-form for our user profile that extends django user model
    '''
    address = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
    town = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
    county = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
    post_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
    country = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
    longitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
    latitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())

    class Meta:
        model = UserProfile
        fields = ('address', 'town', 'county', 'post_code', 'country', 'longitude', 'latitude')