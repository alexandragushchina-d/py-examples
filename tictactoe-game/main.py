
import sys
import string

from tictactoe import *

def main():
  sizeBoard = int(input("Enter a number as a size of your game board: "))
  game = GameTicTacToe(sizeBoard)
  gameBoard = game.startGame()
  game.printGameBoard(gameBoard)
  indexPlayer = int(input("Are you the first or second player? Enter 1 or 2: "))

  while game.moveExist(gameBoard) :
    position = input("Enter your position on the game board - row,col: ")
    posX = int(position.split(",")[0])
    posY = int(position.split(",")[1])
    result = game.nextMove(gameBoard, indexPlayer, posX, posY)
    indexPlayer = game.switchPlayer(indexPlayer)
    if result == 1 or result == 2 :
      print("Player {} has won!!!".format(result))
      break

if __name__ == '__main__':
  sys.exit(main())
