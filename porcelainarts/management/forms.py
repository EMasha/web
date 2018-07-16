from django import forms
from .models import *
from porcelainart.models import *
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib.auth.admin import User
from django import forms

class ProductForm(forms.ModelForm):

    class Meta:
        model = Inventari
        fields = ('kodiI', 'gjendje', 'cmimi_per_njesi', 'cmimi_shitjes', 'pershkrim', 'permasat')

class FurnizimForm(forms.ModelForm):

    class Meta:
        model = Furnizimi
        fields = ('kodiF', 'cmimi_per_njesi', 'sasia', 'pershkrim', 'permasat')

class ShitjeForm(forms.ModelForm):

    class Meta:
        model = Shitje
        fields = ('kodiS', 'sasia', 'ulje', 'cmimi_per_njesi', 'pershkrim', 'klienti', 'kapari', 'data_dorezimit')

class KlientiForm(forms.ModelForm):

    class Meta:
        model = Klienti
        fields = ('emer', 'mbiemer', 'nrTel', 'email')

class ProduktForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'name', 'code', 'slug', 'image', 'description', 'price', 'size', 'available')

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'slug')

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if username and password:
                if not user:
                    raise forms.ValidationError("This user does not exist")
                if not user.check_password(password):
                    raise forms.ValidationError("Incorrect password")
                if not user.is_active:
                    raise forms.ValidationError("This user is not longer active")
            return super(UserLoginForm, self).clean(*args, **kwargs)
