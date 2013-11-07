#Check to see if square (in the form of a list) is a valide sudoku square
#for example [[1,3,2],
#			  [3,2,1],
#			  [2,1,3]]

def check_sudoku(x):
    if check_rows(x) and check_columns(x):
        return True
    return False

# create a correct sudoku row/column to check against
def check_list(length):
    i = 1
    tocheck = []
    while i <= length:
        tocheck.append(i)
        i+=1
    return tocheck

# check each row
def check_rows(x):
    #since it perfect square we can find row length like this
    row_length = len(x)
    check = check_list(row_length)
    #check each row
    for row in x:
        for num in check:
            if num not in row:
                return False
    return True
            
# check each columns
def check_columns(x):
    col_list = []
    col = 0
    row = 0
    check = check_list(len(x))
    while col < len(x):
        while row < len(x):
            col_list.append(x[row][col])
            row += 1
        for num in check:
            if num not in col_list:
                return False
        col += 1
        row = 0
        col_list = []
    return True