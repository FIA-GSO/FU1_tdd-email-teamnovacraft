import pytest

from input_validation import is_valid_email


@pytest.mark.parametrize("email", [
    "test@email.com",
    "t.est@email.com",
    "test@em.ail.com",
    "test@email.co.uk",
    "te-st@email.com",
    "te_st@email.com",
    "test1@email.com",
    "test+text@email.com",
    "test@123.123.123.123",
    "test@[123.123.123.123]",
    "\"test\"@email.com",
    "1234567890@email.com",
    "test@email-domain.com",
    "____@email.com",
    "test.\"text\\why\"@email.com",
    "why.must.\"@\".we.suffer@example.com",
    "very.\"(),:;<>[]\".VERY.\"very@\\\\\\", # do not question it
    "\\\"very\".unusual@strange.example.com"
    "test+other@email.com"
])
def test_is_valid_email__valid_addresses(email):
    # act
    response = is_valid_email(email)

    # assert
    assert response is True


@pytest.mark.parametrize("email", [
    "test email.com",   # Fehlendes @-Zeichen
    "test@email",       # Fehlende Top-Level-Domain
    "test@em@ail.com",  # Mehrfaches @-Zeichen
    "test@email.",      # Fehlende Top-Level-Domain
])
def test_is_valid_email__invalid_addresses(email):
    # act
    response = is_valid_email(email)

    # assert
    assert response is False
