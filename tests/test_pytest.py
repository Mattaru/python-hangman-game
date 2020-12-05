import random
import pytest
import mock
import builtins


# INIT data tests:
# guess_word test
def test_valid_guess_word_without_data(test_obj_without_dict):
    assert test_obj_without_dict.guess_word == ''


def test_valid_guess_word_with_data(test_obj_with_dict):
    assert test_obj_with_dict.guess_word == 'test'


# letter_count test
def test_valid_letter_count_without_data(test_obj_without_dict):
    assert test_obj_without_dict.letter_count == 0


def test_valid_letter_count_with_data(test_obj_with_dict):
    assert test_obj_with_dict.letter_count == 4


# output_word test
def test_valid_output_word_without_data(test_obj_without_dict):
    assert len(test_obj_without_dict.output_word) == 0


# Methods test:
# make_output_row test
def test_make_output_row_without_data(test_obj_without_dict):
    test_obj_without_dict.make_output_row()
    assert test_obj_without_dict.output_word == ''


def test_make_output_row_with_data(test_obj_with_dict):
    test_obj_with_dict.make_output_row()
    output_word_dict = test_obj_with_dict.output_word.split()
    valid = True
    for i in output_word_dict:
        if i != '_':
            valid = False
    assert len(output_word_dict) == 4 and valid


# input_letter test
def test_input_letter(test_obj_with_dict):
    with mock.patch.object(builtins, 'input', lambda _: 't'):
        test_obj_with_dict.input_letter()
        assert test_obj_with_dict.guess_letter == 't'


# guess_letter_valid test
def test_guess_letter_valid_in_word(test_obj_with_dict):
    test_obj_with_dict.make_output_row()
    test_obj_with_dict.guess_letter = 't'
    test_obj_with_dict.guess_letter_valid()
    assert test_obj_with_dict.output_word[0] == 't'
    assert test_obj_with_dict.output_word[6] == 't'
    assert test_obj_with_dict.letter_count == 2
    assert test_obj_with_dict.fails == 0


def test_guess_letter_valid_in_word_couple_times(test_obj_with_dict):
    test_obj_with_dict.make_output_row()
    test_obj_with_dict.guess_letter = 't'
    add_letters = test_obj_with_dict.output_word.split()
    add_letters[0], add_letters[3] = 't', 't'
    test_obj_with_dict.output_word = ' '.join(add_letters)
    test_obj_with_dict.guess_letter_valid()
    assert test_obj_with_dict.output_word[0] == 't'
    assert test_obj_with_dict.output_word[6] == 't'
    assert test_obj_with_dict.fails == 1


def test_guess_letter_valid_not_in_word(test_obj_with_dict):
    test_obj_with_dict.make_output_row()
    test_obj_with_dict.guess_letter = 'p'
    test_obj_with_dict.guess_letter_valid()
    assert not ('p' in test_obj_with_dict.output_word)
    assert test_obj_with_dict.letter_count == 4


# get_answer
def test_get_answer_valid(capfd, test_obj_with_dict):
    test_obj_with_dict.make_output_row()
    test_obj_with_dict.guess_letter = 't'
    test_obj_with_dict.get_answer()
    out, err = capfd.readouterr()
    message = f'{test_obj_with_dict.success_message}\n{test_obj_with_dict.output_word.upper()}' + '\n'
    assert out == message


def test_get_answer_not_valid(capfd, test_obj_with_dict):
    test_obj_with_dict.make_output_row()
    test_obj_with_dict.guess_letter = 'u'
    test_obj_with_dict.get_answer()
    out, err = capfd.readouterr()
    message = f'\n{test_obj_with_dict.fail_message}\n' \
              f'Warning! You are have more {4 - test_obj_with_dict.fails} chances to mistakes\n' \
              f'{test_obj_with_dict.output_word.upper()}' + '\n'
    assert out == message


# end_game test
def test_end_game_defeat(capfd, test_obj_with_dict):
    test_obj_with_dict.fails = 4
    test_obj_with_dict.end_game()
    out, err = capfd.readouterr()
    assert out == test_obj_with_dict.defeat_message + '\n'


def test_end_game_win(capfd, test_obj_with_dict):
    test_obj_with_dict.fails = random.choice([0, 1, 2, 3])
    test_obj_with_dict.end_game()
    out, err = capfd.readouterr()
    assert out == test_obj_with_dict.win_message + '\n'


# start_game_message test
def test_start_start_message(capfd, test_obj_with_dict):
    test_obj_with_dict.start_game_message()
    out, err = capfd.readouterr()
    assert out == f'{test_obj_with_dict.start_message}\n{test_obj_with_dict.output_word.upper()}' + '\n'


# start test
def test_start_without_guess_word(capfd, test_obj_without_dict):
    test_obj_without_dict.start()
    out, err = capfd.readouterr()
    message = "\nSorry, but the dictionary with a words is empty. We can't start the game." + '\n'
    assert out == message


def test_start_with_guess_word(capfd, test_obj_with_dict):
    test_obj_with_dict.fails = 4
    test_obj_with_dict.start()
    out, err = capfd.readouterr()
    assert out == f'{test_obj_with_dict.start_message}\n{test_obj_with_dict.output_word.upper()}\n' \
                  f'{test_obj_with_dict.defeat_message}'+ '\n'
