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
    "FünfundzwanzigZeicheeeeen", # 25 Zeichen, Aa
    "25ZEEEEEEEIIIIIIICHEEEEEN", # 25 Zeichen, A1
    "FÜNFUNDZWANZIGZEICHEN!!!!", # 25 Zeichen, A!
    "25zeeeeeeeiiiiiiicheeeeen", # 25 Zeichen, a1
    "fünfundzwanzig_zeicheeeen", # 25 Zeichen, a!
    "25252522525252525!)((/§!)", # 25 Zeichen, 1!
])
def test_validate_password__valid_passwords(password):
    # act
    response = validate_password(password)

    # assert
    assert response is True


@pytest.mark.parametrize("password", [
    "Lol!1?/",                   #  7 Zeichen, Aa1!
    "Lal4lala",                  #  8 Zeichen, Aa1
    "Luuuu!?!",                  #  8 Zeichen, Aa!
    "L4343!?!",                  #  8 Zeichen, A1!
    "!6ouii?!",                  #  8 Zeichen, a1!
    "AopkdfcksdpokHnkdcnknKKk",  # 24 Zeichen, Aa
    "SDCLJLJDSC21098LJALJ4SAJ",  # 24 Zeichen, A1
    "L$R§X(M$§(M=R§=;X$§FJFW)",  # 24 Zeichen, A!
    "dslkcjalcjewfrf023c2fcm0",  # 24 Zeichen, a1
    "vierundzwanzig_zeicheeen",  # 24 Zeichen, a!
    "7302467/&)(/698&986)/&98",  # 24 Zeichen, 1!
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