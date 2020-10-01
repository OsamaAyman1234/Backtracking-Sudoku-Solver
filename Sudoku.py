board = [
[7,8,0,4,0,0,1,2,0],
[6,0,0,0,7,5,0,0,9],
[0,0,0,6,0,1,0,7,8],
[0,0,7,0,4,0,2,6,0],
[0,0,1,0,5,0,9,3,0],
[9,0,4,0,6,0,0,0,5],
[0,7,0,3,0,0,0,1,2],
[1,2,0,0,0,7,4,0,0],
[0,4,9,2,0,6,0,0,7]
]

def printBoard(board):
	for i in range (len(board)):
		if i%3 == 0 and i != 0:
			print("- - - - - - - - - - - ")
		for j in range (len(board[0])):
			if j%3 == 0 and j != 0:
				print("| ", end = "")
			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j]) + " ", end = "")

def findEmpty(board):
	for i in range (len(board)):
		for j in range (len(board[0])):
			if board[i][j] == 0:
				position = (i,j)
				return position
	return None
				
def valid(board, number, position):
	# check row
	for j in range (len(board[0])):
		if board[position[0]][j] == number and position[1] != j:
			return False
	# check column
	for i in range (len(board)):
		if board[i][position[1]] == number and position[0] != i:
			return False
	# check box
	xbox = position[1] // 3
	ybox = position[0] // 3

	for i in range (ybox * 3, (ybox * 3) + 3):
		for j in range (xbox * 3, (xbox * 3) + 3):
			if board[i][j] == number and (i,j) != position :
				return False

	return True

def solve(board):
	hasEmptyCell = findEmpty(board)
	if not hasEmptyCell:
		return True
	else:
		position = hasEmptyCell
		for i in range (1, 10):
			if valid(board, i, position):
				board[position[0]][position[1]] = i

				if solve(board):
					return True

				board[position[0]][position[1]] = 0

	return False

printBoard(board)
solve(board)
print("- - - - - - - - - - - - - - - - - - - - - Solved")
printBoard(board)