#TODO: Add recursive guessing if the main loop gets stuck

from math import sqrt

def getSudoku():
    sudoku = []
    sudoku.append('000000000')
    sudoku.append('000003085')
    sudoku.append('001020000')
    sudoku.append('000507000')
    sudoku.append('004000100')
    sudoku.append('090000000')
    sudoku.append('500000073')
    sudoku.append('002010000')
    sudoku.append('000040009')
    return sudoku

#Expects list of strings
def formatSudoku(sudoku):
    for i in range(len(sudoku)):
        sudoku[i] = list(sudoku[i])
    #'123...'
    replacewith = ''.join(['%s' % x for x in range(1, len(sudoku[0]) + 1)])
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == '0':
                sudoku[i][j] = replacewith
    return sudoku

def solve(sudoku):
    linelen = len(sudoku)
    smallcube = int(sqrt(linelen))
    solvecount = [ [ 0 for i in range(linelen) ] for j in range(linelen) ]
    while sum(map(sum, solvecount)) < linelen*linelen:
        x = 0
        while x < linelen:
            y = 0
            while y < linelen:
                if len(sudoku[x][y]) == 1:
                    solvecount[x][y] = 1
                else:
                    for i in range(linelen):
                        #Horizontal
                        if len(sudoku[x][i]) == 1 and i != y:
                            sudoku[x][y] = sudoku[x][y].replace(sudoku[x][i], '')
                        #Vertical
                        if len(sudoku[i][y]) == 1 and i != x:
                            sudoku[x][y] = sudoku[x][y].replace(sudoku[i][y], '')
                    #Check if smallcube has all numbers
                    for n in range(int(x/smallcube)*smallcube, int(x/smallcube)*smallcube + smallcube):
                        for m in range(int(y/smallcube)*smallcube, int(y/smallcube)*smallcube + smallcube):
                            if len(sudoku[n][m]) == 1 and n != x and m != y:
                                sudoku[x][y] = sudoku[x][y].replace(sudoku[n][m], '')
                y += 1
            x += 1
        print(sum(map(sum, solvecount)))
    if checksudoku(sudoku):
        return sudoku
    else:
        return false

def checksudoku(sudoku):
    correctline = ''.join(['%s' % x for x in range(1, len(sudoku[0]) + 1)])
    print(''.join(sorted([sudoku[0][j] for j in range(len(sudoku))])))
    for i in range(len(sudoku)):
        #Check if horizontally has all numbers, return if not
        if ''.join(sorted([sudoku[i][j] for j in range(len(sudoku))])) != correctline:
            return False
        #Check if vertically has all numbers, return if not
        if ''.join(sorted([sudoku[j][i] for j in range(len(sudoku))])) != correctline:
            return False
    return True

def printsudoku(sudoku):
    for i in range(len(sudoku)):
        print(sudoku[i])

solve(formatSudoku(getSudoku()))
