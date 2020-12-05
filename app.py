import random

# Enter in to the dictionary all of a words what you wont to be in the game
DICT_OF_WORD = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']

class Hangman:
    def __init__(self, **kwargs):
        try:
            self.guess_word = random.choice(kwargs['dict'])
        except IndexError:
            self.guess_word = ''
        self.fails = 0
        self.letter_count = len(self.guess_word)
        self.output_word = ''
        self.guess_letter = ''
        self.start_message = "\nHallow! We have one of the word from the dictionary of words." \
                             " We do random choice one of it words and then you should try guess this word." \
                             "\nRules:\n1. We show how many letters in the word.\n" \
                             "2. You should try enter the guess letter\n\t" \
                             "- If letter is in the word - we show you where it is.\n\t" \
                             "- If isn't - your fail count had been +1.\n" \
                             "3. Game stops, if your fail count is equal 4," \
                             " or if you are guess all letters in the word.\n" \
                             "\nGood luck!\n"
        self.success_message = '\nGood job! Try again.'
        self.fail_message = 'Sorry, but this letter is not exist.'
        self.win_message = '\nCongratulations! You are win the game!'
        self.defeat_message = '\nSorry, but you are defeat. Try again latter.'

    def make_output_row(self):
        for _ in range(self.letter_count):
            self.output_word += '_ '

    def input_letter(self):
        self.guess_letter = input('Try guess the letter in the word:\n')

    def guess_letter_valid(self):
        if self.guess_letter in self.guess_word and not (self.guess_letter in self.output_word):
            word_changing = self.output_word.split()
            count = 0
            for i in range(len(self.guess_word)):
                if self.guess_letter == self.guess_word[i]:
                    word_changing[i] = self.guess_letter
                    count += 1
            self.output_word = ' '.join(word_changing)
            self.letter_count -= count
            return True
        else:
            self.fails += 1
            return False

    def get_answer(self):
        if self.guess_letter_valid():
            print(f'{self.success_message}\n{self.output_word.upper()}')
        else:
            print(f'\n{self.fail_message}\nWarning! You are have more {4 - self.fails} chances to mistakes\n'
                  f'{self.output_word.upper()}')

    def game_process(self):
        while self.fails != 4 and self.letter_count != 0:
            self.input_letter()
            self.get_answer()

    def end_game(self):
        if self.fails == 4:
            print(self.defeat_message)
        else:
            print(self.win_message)

    def start_game_message(self):
        return print(f'{self.start_message}\n{self.output_word.upper()}')

    def start(self):
        if self.guess_word == '':
            print("\nSorry, but the dictionary with a words is empty. We can't start the game.")
            return
        self.make_output_row()
        self.start_game_message()
        self.game_process()
        self.end_game()


if __name__ == '__main__':
    game = Hangman(dict=DICT_OF_WORD)
    game.start()
