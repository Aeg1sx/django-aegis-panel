from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from api_server.models import User

class CustomUserCreationForm(UserCreationForm):	
    class Meta:
        model = User
        fields = ('email','username','is_staff', 'is_active', 'password')
  
  
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email','username','is_staff', 'is_active', 'password')