import pytest

from blog import factories

@pytest.fixture
def post_published():
    return factories.PostFactory(title='pytest with factory')


@pytest.mark.django_db

def test_post_published(post_published):
    assert post_published.title == 'pytest with factory'
