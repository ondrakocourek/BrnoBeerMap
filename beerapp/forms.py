from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from beerapp.models import Beer, Venue


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FavouriteBeerForm(forms.Form):
    beer = forms.ModelChoiceField(queryset=Beer.objects.all(), label='Vyber oblíbené pivo')

class FavouriteVenueForm(forms.Form):
    venue = forms.ModelChoiceField(queryset=Venue.objects.all(), label='Vyber oblíbený podnik')