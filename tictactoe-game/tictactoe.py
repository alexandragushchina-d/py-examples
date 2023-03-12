
# The game board contains of the list of lists
sizeBoard = 0

def printGameBoard(gameBoard) :
  global sizeBoard
  i = 0
  while i < sizeBoard :
    print("--- "*sizeBoard)
    j = 0
    for j in range(sizeBoard) :
      print("| {} ".format(gameBoard[i][j]), end = '')
    print("\r")
    i += 1
  print("--- "*i)

# Player 1 draws "x" and Player 2 draws "o"
def checkCombination(gameBoard) -> int :
  global sizeBoard
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
  indexOfCell = sizeBoard - 1
  for listNum in gameBoard :
    if listNum[indexOfCell] == "x" :
      count1 += 1
    elif listNum[indexOfCell] == "o" :
      count2 += 1
    indexOfCell -= 1

  return 0

def checkCellEmpty(gameBoard, row, column) -> bool :
	return gameBoard[row-1][column-1] == 0

def switchPlayer(indexPlayer) -> int :
  if indexPlayer == 1 :
    return 2
  else :
    return 1

def moveExist(gameBoard, sizeBoard) -> bool:
  for rowNum in range(sizeBoard) :
    for colNum in range(sizeBoard) :
      if gameBoard[rowNum][colNum] == 0:
        return True
  return False

# draw the next move on the game board
def nextMove(gameBoard, indexPlayer, posX, posY) -> int:
  if indexPlayer == 1 and checkCellEmpty(gameBoard, posX, posY):
    gameBoard[posX-1][posY-1] = "x"
  elif indexPlayer == 2 and checkCellEmpty(gameBoard, posX, posY):
    gameBoard[posX-1][posY-1] = "o"
  printGameBoard(gameBoard)
  return checkCombination(gameBoard)

def startGame(sizeBoard) -> list:
  return [[0, 0, 0] for x in range(sizeBoard)]

if __name__=="__main__":
  sizeBoard = int(input("Enter a number as a size of your game board: "))
  gameBoard = startGame(sizeBoard)
  printGameBoard(gameBoard)
  indexPlayer = int(input("Are you the first or second player? Enter 1 or 2: "))

  while moveExist(gameBoard, sizeBoard) :
    position = input("Enter your position on the game board - row,col: ")
    posX = int(position.split(",")[0])
    posY = int(position.split(",")[1])
    result = nextMove(gameBoard, indexPlayer, posX, posY)
    indexPlayer = switchPlayer(indexPlayer)
    if result == 1 or result == 2 :
      print("Player {} has won!!!".format(result))
      break
