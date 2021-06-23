def isSafe(board, row, col):
    #verifies horizonta line
    for y in range(col):
        if board[row][y] == 1:
            return False
    # verifies diagonal from above
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    # verifies diagonal from below
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True


  
def printSolution(board):
    #gives the output solutions for the several positions in the board 
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    
    

def generateSolution(board, col):
 #gives
    global N, Nsolutions
    if col == N:
        printSolution(board)
        Nsolutions=Nsolutions+1;
        print("Number of solutions ", Nsolutions)
        print()
    # loop em todas as linhas
    for i in range(N):
        if isSafe(board, i, col) == True:
            board[i][col] = 1
            # recursivamente coloca todas as rainhas
            if generateSolution(board, col + 1) == True:
                return True
            # colocar as posições vazias a 0
            board[i][col] = 0
    # backtrack
    return False



Nsolutions=0;
N = int(input('Enter the number of queens:'))
 # int(input())
startCol = 0
board = [[0 for i in range(N)] for j in range(N)]
# print(board)
generateSolution(board, startCol)
