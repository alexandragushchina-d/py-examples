
import sys

from typing import NoReturn

class Hangman:
  def __init__(self, guess_word, temp_guess_word) -> NoReturn  :
    self.guess_word = guess_word
    self.temp_guess_word = temp_guess_word
    self.count = 0

  def guess_letter(self, letter) -> bool :
    return letter in self.guess_word

  def print_try(self, letter) -> NoReturn :
    array_index = [i for i, elem in enumerate(self.guess_word) if elem == letter]
    temp = self.temp_guess_word.split(' ')

    for index in array_index :
      temp[index] = letter

    self.temp_guess_word = ' '.join(temp)
    print(self.temp_guess_word + "\n")

  def check_word(self) -> bool :
    return self.temp_guess_word.count('_') == 0

  def get_stages(self) -> NoReturn :
    stages = ["""
          ------
          |    |
          |
          |
          |
          |
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |
          |
          |
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |    |
          |    |
          |
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |    |
          |    |
          |   /
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |    |
          |    |
          |   / \\
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |  --|
          |    |
          |   / \\
          |
      ------------
      """, """
          ------
          |    |
          |    O
          |  --|--
          |    |
          |   / \\
          |
      ------------
      """]
    print(stages[self.count])
