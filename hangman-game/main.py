
import random
import sys

from urllib.request import urlopen
from hangman import *

def download_pick_word() -> str :
  base_url = 'http://norvig.com/ngrams/sowpods.txt'
  data = urlopen(base_url)

  with open("sowpods_dict.txt", "w") as textfile :
    for line in data :
      textfile.write(line.decode('utf-8'))

  with open("sowpods_dict.txt", "r") as textfile :
    content = textfile.readlines()
    random_index = random.randint(0, len(content))
    guess_word = content[random_index]
    return guess_word

def main() :
  print("Welcome to Hangman!")
  guess_word = download_pick_word()
  temp_guess_word = '_ '*(len(guess_word)-1)
  game = Hangman(guess_word, temp_guess_word)
  print(temp_guess_word)

  while game.count < 6 :
    letter = input("Guess your letter: ").upper()
    if game.guess_letter(letter) :
      game.print_try(letter)
      if game.check_word() == True:
        print("You win. Congratulations!")
        break
    else :
      game.count += 1
      attempt = 6 - game.count
      print("Incorrect!")
      if attempt == 0 :
        print("You don't have any attempts.")
        game.get_stages()
      else :
        print("You have only {} attempts.\n".format(attempt))
        game.get_stages()

  print("Game is over.")
  start_over = input("Do you want to start again? Yes or No: ").lower()
  if start_over == "yes" : main()

if __name__=="__main__" :
  sys.exit(main())
