from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def validate_password(password: str) -> bool:
    if not isinstance(password, str):
        raise TypeError(f'password must be a string. it was {type(password)}')

    types_of_chars = count_types_of_chars(password)
    password_len = len(password)
    if password_len <= 7:
        return False
    if password_len <= 24:
        return types_of_chars == 4
    return types_of_chars >= 2


def count_types_of_chars(text: str) -> int:
    result = 0
    if any(char in ascii_lowercase for char in text):
        result += 1
    if any(char in ascii_uppercase for char in text):
        result += 1
    if any(char in digits for char in text):
        result += 1
    if any(char in punctuation for char in text):
        result += 1
    return result
