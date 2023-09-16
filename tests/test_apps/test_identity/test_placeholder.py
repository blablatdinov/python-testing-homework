import datetime
import pytest
import httpretty

from server.apps.identity.intrastructure.services.placeholder import LeadCreate, LeadUpdate, UserResponse

pytestmark = [
    pytest.mark.django_db,
]


@httpretty.activate(allow_net_connect=False, verbose=True)
def test_create(mixer):
    httpretty.register_uri(httpretty.POST, 'https://domain.com/users', body='{"id": 1}')
    got = LeadCreate('https://domain.com', 5)(user=mixer.blend('identity.User'))

    assert got == UserResponse(id=1)


@httpretty.activate(allow_net_connect=False, verbose=True)
def test_create_with_birthday(mixer):
    httpretty.register_uri(httpretty.POST, 'https://domain.com/users', body='{"id": 1}')
    got = LeadCreate('https://domain.com', 5)(user=mixer.blend(
        'identity.User',
        date_of_birth=datetime.datetime(1965, 6, 14),
    ))

    assert got == UserResponse(id=1)


@httpretty.activate(allow_net_connect=False, verbose=True)
def test_update(mixer):
    httpretty.register_uri(httpretty.PATCH, 'https://domain.com/users/1', body='{"id": 1}')
    LeadUpdate('https://domain.com', 5)(user=mixer.blend('identity.User', lead_id=1))
