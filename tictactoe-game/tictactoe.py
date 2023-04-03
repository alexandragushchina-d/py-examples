
from typing import NoReturn

# The game board contains of the list of lists
class GameTicTacToe :
  def __init__(self, sizeBoard) -> NoReturn  :
    self.sizeBoard = sizeBoard

  def printGameBoard(self, gameBoard) -> NoReturn :
    i = 0
    while i < self.sizeBoard :
      print("--- "*self.sizeBoard)
      j = 0
      for j in range(self.sizeBoard) :
        print("| {} ".format(gameBoard[i][j]), end = '')
      print("\r")
      i += 1
    print("--- "*i)

# Player 1 draws "x" and Player 2 draws "o"
  def checkCombination(self, gameBoard) -> int :
    for listNum in gameBoard :
      if listNum.count("x") == 3 :
        return 1
      elif listNum.count("o") == 3 :
        return 2

    count1 = 0
    count2 = 0
    indexOfCell = 0
    while indexOfCell < len(gameBoard) :
      for listNum in gameBoard :
        if listNum[indexOfCell] == "x" :
          count1 += 1
        elif listNum[indexOfCell] == "o" :
          count2 += 1

      if count1 == 3 :
        return 1
      elif count2 == 3 :
        return 2
      else:
        count1 = 0
        count2 = 0
      indexOfCell += 1

    if count1 == 3 : return 1
    if count2 == 3 : return 2

    count1 = 0
    count2 = 0
    indexOfCell = 0
    for listNum in gameBoard :
      if listNum[indexOfCell] == "x" :
        count1 += 1
      elif listNum[indexOfCell] == "o" :
        count2 += 1
      indexOfCell += 1

    if count1 == 3 : return 1
    if count2 == 3 : return 2

    count1 = 0
    count2 = 0
    indexOfCell = self.sizeBoard - 1
    for listNum in gameBoard :
      if listNum[indexOfCell] == "x" :
        count1 += 1
      elif listNum[indexOfCell] == "o" :
        count2 += 1
      indexOfCell -= 1

    return 0

  def checkCellEmpty(self, gameBoard, row, column) -> bool :
	  return gameBoard[row-1][column-1] == 0

  def switchPlayer(self, indexPlayer) -> int :
    if indexPlayer == 1 :
      return 2
    else :
      return 1

  def moveExist(self, gameBoard) -> bool :
    for rowNum in range(self.sizeBoard) :
      for colNum in range(self.sizeBoard) :
        if gameBoard[rowNum][colNum] == 0:
          return True
    return False

# draw the next move on the game board
  def nextMove(self, gameBoard, indexPlayer, posX, posY) -> int :
    if indexPlayer == 1 and self.checkCellEmpty(gameBoard, posX, posY):
      gameBoard[posX - 1][posY - 1] = "x"
    elif indexPlayer == 2 and self.checkCellEmpty(gameBoard, posX, posY):
      gameBoard[posX - 1][posY - 1] = "o"
    self.printGameBoard(gameBoard)
    return self.checkCombination(gameBoard)

  def startGame(self) -> list :
    return [[0, 0, 0] for x in range(self.sizeBoard)]
