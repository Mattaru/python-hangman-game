import pytest

import app


DICT_OF_WORDS = ['test']
DICT_WITHOUT_WORDS = []


@pytest.fixture()
def test_obj_with_dict():
    return app.Hangman(dict=DICT_OF_WORDS)


@pytest.fixture()
def test_obj_without_dict():
    return app.Hangman(dict=DICT_WITHOUT_WORDS)