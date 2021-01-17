from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api_server.models import User
from api_server.forms import CustomUserCreationForm, CustomUserChangeForm
from board.models import Board

class CustomUser(UserAdmin):
     add_form = CustomUserCreationForm
     form = CustomUserChangeForm
     model = User
admin.site.register(User)
admin.site.register(Board)
