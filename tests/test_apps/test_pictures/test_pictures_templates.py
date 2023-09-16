import pytest
from django.shortcuts import render
from django.test import RequestFactory

pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture()
def favourite_pictures(mixer):
    return mixer.cycle(5).blend('pictures.FavouritePicture')


def test_registration(favourite_pictures):
    page = render(RequestFactory().get('/pictures/favourites'), 'pictures/pages/favourites.html', {
        'object_list': favourite_pictures,
    })


def test_index():
    page = render(RequestFactory().get('/pictures'), 'pictures/pages/index.html')
