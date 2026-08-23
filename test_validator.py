from validator import validate_age, ValidationError
import pytest

def test_zero_age_is_valid():
    assert validate_age(0) == True