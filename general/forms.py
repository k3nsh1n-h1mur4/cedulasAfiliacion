from django.forms import ModelForm
from django import forms

from .models import UserModel, TrabajadorModel, LoginModel

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = '__all__'


class RegistroTrabajadorForm(forms.ModelForm):
    class Meta:
        model = TrabajadorModel
        fields = "__all__"        

class TrUpdateForm(forms.ModelForm):
    class Meta:
        model = TrabajadorModel
        fields = "__all__"


  
