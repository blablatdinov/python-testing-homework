import pytest

from server.apps.pictures.intrastructure.django.forms import FavouritesForm

pytestmark = [
    pytest.mark.django_db,
]


def test_favourites_form(exists_user):
    form = FavouritesForm(user=exists_user)

    form.save(False)