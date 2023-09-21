import pytest

from password import validate_password

"""
Anforderungen der BSI:

ENTWEDER
- mind. 8 Zeichen lang
- mind. 4 verschiedene Zeichenarten (Großbuchstaben, Kleinbuchstaben, Ziffern, Sonderzeichen)

ODER
- mind. 25 Zeichen lang
- mind. 2 verschiedene Zeichenarten
"""

@pytest.mark.parametrize("password", [
    "Lal4laa!",                  #  8 Zeichen, Aa1!
    "fünfundzwanzig_zeicheeeen", # 25 Zeichen, a!
])
def test_validate_password__valid_passwords(password):
    # act
    response = validate_password(password)

    # assert
    assert response is True


@pytest.mark.parametrize("password", [
    "Lal4lala",                  #  8 Zeichen, Aa1
    "vierundzwanzig_zeicheeen",  # 24 Zeichen, a!
    "ABCDEFGHIJKLMNOPQRSTUVWXY", # 25 Zeichen, A
    "abcdefghijklmnopqrstuvwxy", # 25 Zeichen, a
    "1208925819614630000000000", # 25 Zeichen, 1
    "!?!?!?!?!?!!?!?!?!?!?!!?!", # 25 Zeichen, !
])
def test_validate_password__invalid_passwords(password):
    # act
    response = validate_password(password)

    # assert
    assert response is False