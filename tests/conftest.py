"""
This module is used to provide configuration, fixtures, and plugins for pytest.

It may be also used for extending doctest's context:
1. https://docs.python.org/3/library/doctest.html
2. https://docs.pytest.org/en/latest/doctest.html
"""
import pytest

from django.test.client import Client

pytest_plugins = [
    # Should be the first custom one:
    'plugins.django_settings',

    # TODO: add your own plugins here!
]


@pytest.fixture()
def mixer():
    from mixer.backend.django import mixer
    return mixer


@pytest.fixture()
def exists_user(mixer):
    return mixer.blend('identity.User')


@pytest.fixture()
def user_client(exists_user, client: Client):
    client.force_login(exists_user)
    return client
