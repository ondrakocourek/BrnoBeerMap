from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("venues/", views.venue_list, name="venue_list"),
    path("beers/", views.beer_list, name="beer_list"),
    path("venue/<int:venue_id>/", views.venue_detail, name="venue_detail"),
    path("profile/", views.user_profile, name="user_profile"),
    path("register/", views.register, name="register"),
    path('favourite/beer/<int:beer_id>/remove/', views.remove_favourite_beer, name='remove_favourite_beer'),
    path('favourite/venue/<int:venue_id>/remove/', views.remove_favourite_venue, name='remove_favourite_venue'),
    path('venues-by-beer/', views.venues_by_beer, name='venues_by_beer'),


]