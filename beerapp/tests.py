import pytest

"testing of availability of main page"
@pytest.mark.django_db
def test_home_view(client):
    response = client.get('/')
    assert response.status_code == 200


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
