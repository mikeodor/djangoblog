from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class registerform(UserCreationForm):
    email=forms.EmailField()
    first_name=forms.Textarea()
    last_name=forms.Textarea()
    

       
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']



class userupdateform(forms.ModelForm):
    email=forms.EmailField()
    first_name=forms.Textarea()
    last_name=forms.Textarea()
    

       
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class profileupdate(forms.ModelForm):
    class Meta:
        model= Profile
        fields=['coverpic','profilepic']