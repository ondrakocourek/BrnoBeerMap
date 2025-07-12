import pytest
from django.test import TestCase

def test_home_view(client):
    response = client.get('/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_profile_view_authenticated(client, django_user_model):
    user = django_user_model.objects.create_user(username='tester', password='testpass')
    client.login(username='tester', password='testpass')
    response = client.get('/profile/')
    assert response.status_code == 200
    assert b'Oblíbená piva' in response.content
