sudoku=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# Print the sudoku
def print_sudoku():
    for i in sudoku:
        for j in i:
            print(j,end=" ")
        print()

# Checks if that value is present in the row
def check_row(val,row):
    for i in range(9):
        if sudoku[row][i]==val:
            return True
    return False

# To check if that value if present in the column
def check_col(val,col):
    for i in range(9):
        if sudoku[i][col]==val:
            return True
    return False

# Checks if the value is present in the box.
def check_box(val,row,col):
    x = row//3
    y = col//3
    for i in range(3*x,3*(x+1)):
        for j in range(3*y,3*(y+1)):
            if sudoku[i][j]==val:
                return True
    return False

# Solve the sudoku
def sudoku_solver(pos=0):
    row = pos//9
    col = pos%9
    if row == 9:
        print_sudoku()
        return
    if sudoku[row][col]!=0:
        sudoku_solver(pos+1)
    else:
        for i in range(1,10):
            if ( (not check_row(i,row)) and (not check_col(i,col)) and (not check_box(i,row,col))):
                sudoku[row][col]=i
                sudoku_solver(pos+1)
                sudoku[row][col]=0
        
print_sudoku()
print()
sudoku_solver()
