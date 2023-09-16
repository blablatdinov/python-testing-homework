import pytest


pytestmark = [
    pytest.mark.django_db,
]


@pytest.fixture()
def favour_picture(mixer, exists_user):
    return mixer.blend('pictures.FavouritePicture', user_id=exists_user.id, foreign_id=89)


def test_str(favour_picture, exists_user):
    assert str(favour_picture) == '<Picture 89 by {0}>'.format(exists_user.id)
