from django.contrib import admin
from .models import BeerType, Beer, CityDistrict, Venue, FavouriteVenue, FavouriteBeer

admin.site.register(BeerType)
admin.site.register(Beer)
admin.site.register(CityDistrict)
admin.site.register(Venue)
admin.site.register(FavouriteVenue)
admin.site.register(FavouriteBeer)
