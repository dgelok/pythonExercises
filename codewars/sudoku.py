def sudoku(puzzle):

    possibilities = {}
    notDone = True
    for i in range(9):
        possibilities[i] = {}
    for i in range(9):
        for j in range(9):
            possibilities[i][j] = [1,2,3,4,5,6,7,8,9]

    while notDone:
        for horiz in range(9):
            for vert in range (9):
                if puzzle[horiz][vert] == 0:
                    #check verticals and horizontals, remove items from list.
                    for i in range(9):
                        if puzzle[horiz][i] in possibilities[horiz][vert]:
                            possibilities[horiz][vert].remove(puzzle[horiz][i])
                    for i in range(9):
                        if puzzle[i][vert] in possibilities[horiz][vert]:
                            possibilities[horiz][vert].remove(puzzle[i][vert])
                    
                    if 0 <= horiz < 3:
                        horizRange = [0, 1, 2]
                    elif 3 <= horiz < 6:
                        horizRange = [3, 4, 5]
                    else:
                        horizRange = [6, 7, 8]
                    
                    if 0 <= vert < 3:
                        vertRange = [0, 1, 2]
                    elif 3 <= vert < 6:
                        vertRange = [3, 4, 5]
                    else:
                        vertRange = [6, 7, 8]

                    for i in range(3):
                        for j in range(3):
                            if puzzle[horizRange[i]][vertRange[j]] in possibilities[horiz][vert]:
                                possibilities[horiz][vert].remove(puzzle[horizRange[i]][vertRange[j]])

                    if len(possibilities[horiz][vert]) == 1:
                        puzzle[horiz][vert] = possibilities[horiz][vert][0]
        





        notDone = False
        for horiz in range(9):
            for vert in range(9):
                if puzzle[horiz][vert] == 0:
                    notDone = True
                

    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)