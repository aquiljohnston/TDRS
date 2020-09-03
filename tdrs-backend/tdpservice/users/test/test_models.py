"""Module for testing the user model."""
import pytest

from ..models import Region, STT


@pytest.mark.django_db
def test_user_string_representation(user):
    """Test user string representation."""
    assert str(user) == user.username


@pytest.mark.django_db
def test_region_string_representation(stts):
    """Test region string representation."""
    assert str(Region.objects.first()) == "1"


@pytest.mark.django_db
def test_stt_string_representation(stts):
    """Test STT string representation."""
    assert str(STT.objects.filter(type=STT.STTType.STATE).first()) == "Alabama"
