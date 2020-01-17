#from django import forms


#class UserLoginForm(forms.Form):
#    """Form to be used to log users in"""

#    username = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)

#from django.shortcuts import render, redirect, reverse
#from django.contrib import auth, messages
#from accounts.forms import UserLoginForm

#def index(request):
#    """Return the index.html file"""
#    return render(request,  'index.html')


#def logout(request):
#    """Log the user out"""
#    auth.logout(request)
#    messages.success(request, "You have successfully been logged out")
#    return redirect(reverse('index'))


#def login(request):
#    """Return a login page"""
#    if request.method == "POST":
#        login_form = UserLoginForm(request.POST)

#        if login_form.is_valid():
#            user = auth.authenticate(username=request.POST['username'],
#                                    password=request.POST['password'])
            

#            if user:
#                auth.login(user=user, request=request)
#                messages.success(request, "You have successfully logged in!")
#            else:
#                login_form.add_error(None, "Your username or password is incorrect")
#    else:
#        login_form = UserLoginForm()
#    return render(request, 'login.html', {'login_form': login_form})

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form to be used to log users in"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
#----add------->  
def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2

        
