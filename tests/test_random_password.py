import sys
sys.dont_write_bytecode = True

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
    assert all(char in passwd.letters_uc for char in password1)

    password2 = passwd.Random_password(length=length, lowercase=True)
    assert all(char in passwd.letters_lc for char in password2)

    password3 = passwd.Random_password(length=length, digits=True)
    assert all(char in passwd.digits for char in password3)

    password4 = passwd.Random_password(length=length, special=True)
    assert all(char in passwd.special for char in password4)



def test_randomness_for_password(passwd, length):
    
    password1 = passwd.Random_password(length, uppercase=True,
                    lowercase=True, digits=True, special=True)

    password2 = passwd.Random_password(length, uppercase=True,
                    lowercase=True, digits=True, special=True)
    
    if length != 0:
        assert password1 != password2
    else:
        assert password1 == "" and password2 == ""
