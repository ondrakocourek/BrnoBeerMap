import pytest
from django.urls import reverse
from beerapp.models import Beer, Venue, FavouriteBeer, FavouriteVenue

"testing of availability of main page"
@pytest.mark.django_db
def test_home_view(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Brno" in response.content



"test for module beer"
@pytest.mark.django_db
def test_beer_str_representation():
    from beerapp.models import Beer
    beer = Beer.objects.create(name="Plzeň 12")
    assert str(beer) == "Plzeň 12"


"test for adding favourite beer for test user"
@pytest.mark.django_db
def test_add_favourite_beer(client, django_user_model):
    from beerapp.models import Beer, FavouriteBeer

    beer = Beer.objects.create(name="Test Beer")
    user = django_user_model.objects.create_user(username='tester', password='testpass')
    client.login(username='tester', password='testpass')

    response = client.post('/profile/', {'add_beer': '', 'beer': beer.id})

    assert FavouriteBeer.objects.filter(user=user, beer=beer).exists()


"test for nonlogged user"
def test_profile_view_requires_login(client):
    url = reverse("user_profile")
    response = client.get(url)
    assert response.status_code == 302


"test for adding beer to venue, after that test try filter and response if it find the venue"
@pytest.mark.django_db
def test_venues_by_beer_view(client):
    beer = Beer.objects.create(name="Pilsner")
    venue = Venue.objects.create(name="Testovaci hospoda")
    venue.beers.add(beer)
    response = client.get(reverse("venues_by_beer") + f"?beer={beer.id}")
    assert response.status_code == 200
    assert b"Testovaci hospoda" in response.content


"testing if venue_detail is available and that it have a right respond"
@pytest.mark.django_db
def test_venue_detail_view(client):
    venue = Venue.objects.create(name="Testovaci hospoda")
    response = client.get(reverse("venue_detail", args=[venue.id]))
    assert response.status_code == 200
    assert b"Testovaci hospoda" in response.content