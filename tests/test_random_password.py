import pytest
from random import choice
from src.random_password import Password

@pytest.fixture
def passwd():
    return Password()


@pytest.fixture
def length():
    return choice(range(0, 100))


def test_shuffle(passwd):
    a = "random string"
    assert passwd._secure_shuffle(list(a)) != passwd._secure_shuffle(list(a))

@pytest.mark.parametrize("lengths", range(0, 101, 2))
def test_password_generation_with_different_lengths(passwd, lengths):
    password = passwd.Random_password(length=lengths, uppercase=True,
                lowercase=True, digits=True, special=True)

    if lengths == 0:
        assert len(password) == 0
        assert password == ""

    else:
        assert len(password) == lengths


def test_password_characters(passwd, length):

    password1 = passwd.Random_password(length=length, uppercase=True)
    assert password1.isupper()

    password2 = passwd.Random_password(length=length, lowercase=True)
    assert password2.islower()

    password3 = passwd.Random_password(length=length, digits=True)
    assert password3.isdigit()

    password4 = passwd.Random_password(length=length, special=True)
    assert all(char in passwd.special for char in password4)



def test_randomness_for_password(passwd, length):
    
    password1 = passwd.Random_password(length, uppercase=True,
                    lowercase=True, digits=True, special=True)

    password2 = passwd.Random_password(length, uppercase=True,
                    lowercase=True, digits=True, special=True)

    assert password1 != password2
