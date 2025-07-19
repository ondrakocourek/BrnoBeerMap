from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from beerapp.models import Beer, Venue

"form for user registration"
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


"form for adding user's favourite beer"
class FavouriteBeerForm(forms.Form):
    beer = forms.ModelChoiceField(queryset=Beer.objects.all(), label='Vyber oblíbené pivo')


"form for adding user's favourite venue"
class FavouriteVenueForm(forms.Form):
    venue = forms.ModelChoiceField(queryset=Venue.objects.all(),
    label='Vyber oblíbený podnik')

