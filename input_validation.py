import re

EMAIL_REGEX = re.compile(r'[\w.-]+@[\w.-]+\.\w+')


def is_valid_email(email: str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """
    return re.fullmatch(EMAIL_REGEX, email) is not None
