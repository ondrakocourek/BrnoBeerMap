from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Venue, Beer, FavouriteBeer, FavouriteVenue
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
from .forms import FavouriteBeerForm, FavouriteVenueForm
from .models import FavouriteBeer, FavouriteVenue


"Main page"
def home(request):
    venues = Venue.objects.all()
    return render(request, "beerapp/home.html", {"venues": venues})

"Represents a list of beers"
def beer_list(request):
    beers = Beer.objects.all()
    return render(request, "beerapp/beers.html", {"beers": beers})


"Represents a list of venues"
def venue_list(request):
    venues = Venue.objects.all()
    return render(request, "beerapp/venue_list.html", {"venues": venues})

"represents a detailed view for venues, consists of type, address, open hours and type of beers served"
def venue_detail(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    return render(request, "venue_detail.html", {"venue": venue})

"""
def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, "user_profile.html", {"user": user})
"""


"user profile with favourite beers and venues, with ability to add or remove"
@login_required
def user_profile(request):
    user = request.user
    favourite_beers = FavouriteBeer.objects.filter(user=user)
    favourite_venues = FavouriteVenue.objects.filter(user=user)

    if request.method == "POST":
        if 'add_beer' in request.POST:
            beer_form = FavouriteBeerForm(request.POST)
            if beer_form.is_valid():
                beer = beer_form.cleaned_data['beer']
                FavouriteBeer.objects.get_or_create(user=user, beer=beer)
                return redirect('user_profile')
        elif 'add_venue' in request.POST:
            venue_form = FavouriteVenueForm(request.POST)
            if venue_form.is_valid():
                venue = venue_form.cleaned_data['venue']
                FavouriteVenue.objects.get_or_create(user=user, venue=venue)
                return redirect('user_profile')
    else:
        beer_form = FavouriteBeerForm()
        venue_form = FavouriteVenueForm()

    return render(request, "beerapp/user_profile.html", {
        "favourite_beers": favourite_beers,
        "favourite_venues": favourite_venues,
        "beer_form": beer_form,
        "venue_form": venue_form,
    })


"registration of new user"
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Účet byl vytvořen! Můžeš se přihlásit.")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "beerapp/register.html", {"form": form})


"function to switch status of favourite venue add/or remove depends if exists"
@login_required
def toggle_favourite_venue(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    fav, created = FavouriteVenue.objects.get_or_create(user=request.user, venue=venue)
    if not created:
        fav.delete()
    return redirect("user_profile")

"function to add/remove favourite beer"
@login_required
def toggle_favourite_beer(request, beer_id):
    beer = get_object_or_404(Venue, id=beer_id)
    fav, created = FavouriteBeer.objects.get_or_create(user=request.user, beer=beer)
    if not created:
        fav.delete()
    return redirect("user_profile")


"function for removing favourite beer"
@login_required
def remove_favourite_beer(request, beer_id):
    if request.method == "POST":
        fav = get_object_or_404(FavouriteBeer, user=request.user, beer_id=beer_id)
        fav.delete()
    return redirect('user_profile')


"function for removing favourite venue"
@login_required
def remove_favourite_venue(request, venue_id):
    if request.method == "POST":
        fav = get_object_or_404(FavouriteVenue, user=request.user, venue_id=venue_id)
        fav.delete()
    return redirect('user_profile')



"represents which venues serves which kind of beer"
def venues_by_beer(request):
    selected_beer_id = request.GET.get('beer')
    beers = Beer.objects.all()
    venues = Venue.objects.all()

    if selected_beer_id:
        try:
            selected_beer_id = int(selected_beer_id)
            venues = venues.filter(beers__id=selected_beer_id)
        except ValueError:
            selected_beer_id = None

    context = {
        'beers': beers,
        'venues': venues,
        'selected_beer_id': selected_beer_id,
    }

    return render(request, 'beerapp/venues_by_beer.html', context)