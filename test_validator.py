from validator import validate_age, ValidationError
import pytest


def test_valid_age():
    assert validate_age(25) == True


def test_negative_age_rejected():
    with pytest.raises(ValidationError):
        validate_age(-5)


def test_non_integer_rejected():
    with pytest.raises(ValidationError):
        validate_age("25")


def test_zero_age_is_valid():
    assert validate_age(0) == True