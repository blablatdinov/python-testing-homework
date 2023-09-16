from server.apps.identity.models import User
import pytest

pytestmark = [
    pytest.mark.django_db,
]


def test(client):
    got = client.get('/identity/login')

    assert got.status_code == 200


def test_registration(client):
    got = client.post('/identity/registration', data={
        'email': 'my@email.com',
        'first_name': 'My name',
        'last_name': 'My name',
        'date_of_birth': '1970-09-18',
        'address': 'My name',
        'job_title': 'My name',
        'phone': 'My name',
        'password1': 'My name',
        'password2': 'My name',
    })

    assert got.status_code == 302
    assert got.headers['location'] == '/identity/login'
    assert User.objects.count() == 1
