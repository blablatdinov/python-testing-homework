import pytest

from server.apps.pictures.models import FavouritePicture

pytestmark = [
    pytest.mark.django_db,
]


def test_get(user_client):
    got = user_client.get('/pictures/dashboard')

    assert got.status_code == 200


def test_create(user_client, exists_user):
    got = user_client.post('/pictures/dashboard', data={
        'foreign_id': 1,
        'url': 'https://via.placeholder.com/600/92c952',
    })

    assert got.status_code == 302
    assert got.headers['location'] == '/pictures/dashboard'
    assert FavouritePicture.objects.filter(
        user_id=exists_user.id,
        foreign_id=1,
        url='https://via.placeholder.com/600/92c952',
    ).count() == 1


def test_get_favourites(user_client):
    got = user_client.get('/pictures/favourites')

    assert got.status_code == 200
