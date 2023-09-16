import pytest
from server.apps.identity.models import User

pytestmark = [
    pytest.mark.django_db,
]


def test_without_email():
    with pytest.raises(ValueError):
        User.objects.create_user(email='', password='SeCr3t')
