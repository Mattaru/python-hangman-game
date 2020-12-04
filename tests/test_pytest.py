import pytest
import mock
import builtins

import app


DICT_OF_WORDS = ['test']
DICT_WITHOUT_WORDS = []


# INIT data tests:
# guess_word test
def test_valid_guess_word_without_data():
    test_obj = app.Hangman(dict=DICT_WITHOUT_WORDS)
    assert test_obj.guess_word == ''

def test_valid_guess_word_with_data():
    test_obj = app.Hangman(dict=DICT_OF_WORDS)
    assert test_obj.guess_word == 'test'

# letter_count test
def test_valid_letter_count_without_data():
    test_obj = app.Hangman(dict=DICT_WITHOUT_WORDS)
    assert test_obj.letter_count == 0

def test_valid_letter_count_with_data():
    test_obj = app.Hangman(dict=DICT_OF_WORDS)
    assert test_obj.letter_count == 4

# output_word test
def test_valid_output_word_without_data():
    test_obj = app.Hangman(dict=DICT_WITHOUT_WORDS)
    assert len(test_obj.output_word) == 0

# Methods test:
# make_output_row test
def test_make_output_row_without_data():
    test_obj = app.Hangman(dict=DICT_WITHOUT_WORDS)
    test_obj.make_output_row()
    assert test_obj.output_word == ''

def test_make_output_row_with_data():
    test_obj = app.Hangman(dict=DICT_OF_WORDS)
    test_obj.make_output_row()
    output_word_dict = test_obj.output_word.split()
    valid = True
    for i in output_word_dict:
        if i != '_':
            valid = False
    assert len(output_word_dict) == 4 and valid

# input_letter test
def test_input_letter():
    test_obj = app.Hangman(dict=DICT_OF_WORDS)
    with mock.patch.object(builtins, 'input', lambda _: 't'):
        test_obj.input_letter()
        assert test_obj.guess_letter == 't'

# guess_letter_valid test
def test_guess_letter_valid_in_word():
    test_obj = app.Hangman(dict=DICT_OF_WORDS)
    test_obj.make_output_row()
    test_obj.guess_letter = 't'
    test_obj.guess_letter_valid()
    assert (test_obj.output_word[0] and test_obj.output_word[6]) == 't' \
           and test_obj.letter_count == 2 \
           and test_obj.fails == 0

def test_guess_letter_valid_in_word_couple_times():
    test_obj = app.Hangman(dict=DICT_OF_WORDS)
    test_obj.make_output_row()
    test_obj.guess_letter = 't'
    add_letters = test_obj.output_word.split()
    add_letters[0], add_letters[3] = 't', 't'
    test_obj.output_word = ' '.join(add_letters)
    test_obj.guess_letter_valid()
    assert (test_obj.output_word[0] and test_obj.output_word[6]) == 't' \
           and test_obj.fails == 1

def test_guess_letter_valid_not_in_word():
    test_obj = app.Hangman(dict=DICT_OF_WORDS)
    test_obj.make_output_row()
    test_obj.guess_letter = 'p'
    test_obj.guess_letter_valid()
    assert not ('p' in test_obj.output_word) and test_obj.letter_count == 4


