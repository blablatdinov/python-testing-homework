from django.shortcuts import render
from django.test import RequestFactory

from server.apps.identity.intrastructure.django.forms import RegistrationForm


def test_registration():
    page = render(RequestFactory().get('/identity/registration'), 'identity/pages/registration.html', {
        'form': RegistrationForm(),
    })
