import logging

logger = logging.getLogger("validator")
logging.basicConfig(level=logging.INFO)


class ValidationError(Exception):
    """Raised when a value fails validation."""


def validate_age(age):
    if not isinstance(age, int) or isinstance(age, bool):
        raise ValidationError("age must be a whole number")
    if age < 0:
        raise ValidationError("age must not be negative")
    logger.info("age %s is valid", age)
    return True