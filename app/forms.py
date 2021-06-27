from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
  password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
  email=forms.CharField(required=True,label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
  class Meta:
    model=User
    fields=['username','email','password1','password2']
    labels={'email':'Email'}
    widgets={
      'username':forms.TextInput(attrs={'class':'form-control'}),
      
    }


# login form
class LoginForm(AuthenticationForm):
  username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder':'Enter the Username'}))

  password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control','placeholder':'Enter the Password'}))


# passwordchange form
class CustomerPasswordChangeForm(PasswordChangeForm):
  old_password=forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
  
  new_password1 =forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html) 

  new_password2 =forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'})) 


# password reset

class MyPasswordReset(PasswordResetForm):
  email=forms.EmailField(label=_('Email'),max_length=254,
  widget=forms.EmailInput(attrs={
    'autocomplete':'email','class':'form-control'
  }))

# password Reset Confirm

class MySetPasswordForm(SetPasswordForm):
  new_password1 =forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html) 

  new_password2 =forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'})) 



# model form for profile
class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model=Customer
    fields=['name','locality','city','state','zipcode',]
    widgets={
      'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Full Name'}),
      'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Address'}),
      'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the City Name'}),
      'state':forms.Select(attrs={'class':'form-control'}),
      'zipcode':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the  Zip Code'}),
    }