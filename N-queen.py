# Function to check if two queens threaten each other or not
def isSafe(mat, r, c):
 
    # return false if two queens share the same column
    for i in range(r):
        if mat[i][c] == 'Q':
            return False
 
    # return false if two queens share the same `` diagonal
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
 
    # return false if two queens share the same `/` diagonal
    (i, j) = (r, c)
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
 
    return True
 
 
def printSolution(mat):
    for r in mat:
        print(str(r).replace(',', '').replace('\'', ''))
    print()
 
 
def nQueen(mat, r):
 
    # if `N` queens are placed successfully, print the solution
    if r == len(mat):
        printSolution(mat)
        return
 
    # place queen at every square in the current row `r`
    # and recur for each valid movement
    for i in range(len(mat)):
 
        # if no two queens threaten each other
        if isSafe(mat, r, i):
            # place queen on the current square
            mat[r][i] = 'Q'
 
            # recur for the next row
            nQueen(mat, r + 1)
 
            # backtrack and remove the queen from the current square
            mat[r][i] = '–'
 
 
if __name__ == '__main__':
 
    # `N × N` chessboard
    N = int(input("Enter a number: "))
 
    # `mat[][]` keeps track of the position of queens in
    # the current configuration
    mat = [['–' for x in range(N)] for y in range(N)]
 
    nQueen(mat, 0)




  
  

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
