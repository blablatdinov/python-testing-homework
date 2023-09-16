import pytest
from django.shortcuts import render
from django.test import RequestFactory

pytestmark = [
    pytest.mark.django_db,
]


def test_base():
    page = render(RequestFactory().get('/'), 'common/_base.html')


def test_messages():
    page = render(RequestFactory().get('/'), 'common/includes/messages.html', {
        'messages': ['First', 'second'],
    })
