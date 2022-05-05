global N 
N = int(input("enter the number "))
 
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j], end = " ")
        print()
 

def isSafe(board, row, col):
 
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True
 
def solveNQUtil(board, col):
     
  
    if col >= N:
        for row in range(N):
            for col in range(N):
                print(board[row][col],end =' ')
            print( )
        print( )
        return 
 

    for i in range(N):
 
        if isSafe(board, i, col):
             
   
            board[i][col] = 1
 
        
            solveNQUtil(board, col + 1)
            board[i][col] = 0
 
 
def solveNQ():
    board = [ [0 for row in range(N)]for col in range(N) ]
 
    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist")
        return False
    return True
 
# Driver Code
solveNQ()
