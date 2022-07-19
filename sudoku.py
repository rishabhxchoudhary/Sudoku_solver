sudoku=[
[0,4,0,0,1,0,9,0,8],
[8,0,5,0,0,0,7,0,0],
[0,0,0,0,0,0,0,1,0],
[0,2,0,0,0,5,0,0,4],
[0,0,1,6,0,0,0,0,0],
[0,3,0,0,0,8,0,0,2],
[0,0,0,0,0,0,0,6,0],
[3,0,4,0,0,0,8,0,0],
[0,8,0,0,9,0,4,0,3]
]

def IsInRow(val,row):
    if val in sudoku[row]: return True
    return False

def IsInCol(val,col):
    for i in range(9):
        if sudoku[i][col]==val:
            return True
    return False

def IsInSubMatrix(val,row,col):
    x = row//3
    y = col//3
    for i in range(3*x, 3*(x+1)):
        for j in range(3*y,3*(y+1)):
            if sudoku[i][j]==val: return True
    return False

def print_sudoku():
    for i in sudoku:
        for j in i:
            print(j,end=" ")
        print()

print_sudoku()
print()

def solve_sudoku(pos=0):
    row = pos//9
    col = pos%9
    if row==9:
        print_sudoku()
        return
    if sudoku[row][col]!=0: 
        solve_sudoku(pos+1)
    else:
        for i in range(1,10):
            if ( not IsInRow(i,row) and (not IsInCol(i,col)) and (not IsInSubMatrix(i,row,col)) ):
                sudoku[row][col]=i
                solve_sudoku(pos+1)
                sudoku[row][col]=0
solve_sudoku(0)
