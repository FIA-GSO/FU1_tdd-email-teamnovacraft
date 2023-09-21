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
    "test+other@email.com"
])
def test_is_valid_email__valid_addresses(email):
    # act
    response = is_valid_email(email)

    # assert
    assert response is True


@pytest.mark.parametrize("email", [
    "test email.com",
    "test@email",
    "test@em@ail.com"
])
def test_is_valid_email__invalid_addresses(email):
    # act
    response = is_valid_email(email)

    # assert
    assert response is False
