from django.contrib.auth.models import User
from django.db import models

class BeerType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Beer(models.Model):
    name = models.CharField(max_length=100)
    beertype = models.ManyToManyField(BeerType, related_name="beers")
    def __str__(self):
        return self.name

class CityDistrict(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Venue(models.Model):
    VENUE_TYPES = (
        ("pub", "Pub"),
        ("restaurant", "Restaurant"),
        ("brewery", "Brewery"),
    )
    name = models.CharField(max_length=200)
    address = models.TextField()
    venue_type = models.CharField(max_length=20, choices=VENUE_TYPES)
    beers = models.ManyToManyField(Beer, related_name="venues")
    districts = models.ManyToManyField(CityDistrict, related_name="venues")
    website = models.URLField(blank=True, null=True)
    opening_hours = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class FavouriteVenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favourite venue is: {self.venue.name}"

class FavouriteBeer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s favourite beer is: {self.beer.name}"