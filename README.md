# Sudoku-Solver

Currently the coding on this is quite 'ugly'
When I am satisfied with the overall result I plan to go back and tidy it up considerably.

Takes a nested list where each sub list is the row.
0 values represent empty/unknown values of the sudoku.

At the moment, it solves for where there is only one number available for row, column and box
It also looks for each row where there is only one place a number could go FOR ROWS ONLY.
The next stage to be added to this so it can solve more complex sudkous is to code this for columns and boxes also.

E.g.
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

Have successfully solved:
grid = [[ 0,0,8,0,0,9,0,0,0],
        [ 6,2,0,0,7,0,0,0,5],
        [ 3,0,4,0,0,0,8,0,0],
        [ 0,0,0,4,2,0,0,0,0],
        [ 2,0,0,9,1,0,0,8,7],
        [ 7,9,1,6,0,0,0,0,4],
        [ 5,8,0,1,3,2,4,0,9],
        [ 4,3,7,5,9,8,1,6,9],
        [ 0,0,2,0,0,0,5,0,0]]
    An 'easy' sudoku

Has successfully solved:
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
