import pytest

from django.conf import settings


def test_ensure_correct_settings():
    """Test if TEST_SETTING exists."""
    assert settings.TEST_SETTING == 1
