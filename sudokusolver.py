from collections import Counter
from itertools import chain

def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def make_columns_boxes(grid):
    columns = []

    for i in range(9):
        columns.append([item[i] for item in grid])

    # list should have
    n = 3
    boxes = []
    final_boxes = []
    for row in grid:

        x = list(divide_chunks(row, n))
        boxes.append(x)


    for i in range(3):
        f_boxes = []

        for y in boxes:
            f_boxes.append(y[i])
        
        final_boxes.append(f_boxes)

    the_boxes = []
    for box in final_boxes:
        z = list(divide_chunks(box, n))
        for i in range(0,3):
            z[i] = [x for l in z[i] for x in l]
            the_boxes.append(z[i])
    
    return the_boxes, columns

def solving_iteration(grid):
    rownumber = 0

    for row in grid:

        columnnumber = 0
        for x in row:

            if x == 0:

                if rownumber <= 2:
                    boxnumber = 0 
                elif rownumber >= 6:
                    boxnumber = 2
                else:
                    boxnumber = 1

                if columnnumber > 2 and columnnumber < 6 and boxnumber == 0:
                    boxnumber = 3
                elif columnnumber > 2 and columnnumber < 6 and boxnumber == 1:
                    boxnumber = 4
                elif columnnumber > 2 and columnnumber < 6 and boxnumber == 2:
                    boxnumber = 5    
                elif columnnumber >= 6 and boxnumber == 0:
                    boxnumber = 6
                elif columnnumber >= 6 and boxnumber == 1:
                    boxnumber = 7
                elif columnnumber >= 6 and boxnumber == 2:
                    boxnumber = 8 

                the_boxes, columns = make_columns_boxes(grid)

                value = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                for n in set(grid[rownumber]):
                    try:
                        value.remove(n)
                    except ValueError:
                        continue
                
                for n in set(columns[columnnumber]):
                    try:
                        value.remove(n)
                    except ValueError:
                        continue

                for n in set(the_boxes[boxnumber]):
                    try:
                        value.remove(n)
                    except ValueError:
                        continue
                
                if len(value) == 1:
                    grid[rownumber][columnnumber] = value[0]

            columnnumber += 1
        
        rownumber += 1

    return grid

def finding_singles(grid):
    rownumber = 0

    for row in grid:
        unknowns = []

        columnnumber = 0
        for x in row:

            if x == 0:

                if rownumber <= 2:
                    boxnumber = 0 
                elif rownumber >= 6:
                    boxnumber = 2
                else:
                    boxnumber = 1

                if columnnumber > 2 and columnnumber < 6 and boxnumber == 0:
                    boxnumber = 3
                elif columnnumber > 2 and columnnumber < 6 and boxnumber == 1:
                    boxnumber = 4
                elif columnnumber > 2 and columnnumber < 6 and boxnumber == 2:
                    boxnumber = 5    
                elif columnnumber >= 6 and boxnumber == 0:
                    boxnumber = 6
                elif columnnumber >= 6 and boxnumber == 1:
                    boxnumber = 7
                elif columnnumber >= 6 and boxnumber == 2:
                    boxnumber = 8 

                the_boxes, columns = make_columns_boxes(grid)

                value = [1, 2, 3, 4, 5, 6, 7, 8, 9]

                for n in set(grid[rownumber]):
                    try:
                        value.remove(n)
                    except ValueError:
                        continue
                
                for n in set(columns[columnnumber]):
                    try:
                        value.remove(n)
                    except ValueError:
                        continue

                for n in set(the_boxes[boxnumber]):
                    try:
                        value.remove(n)
                    except ValueError:
                        continue

                unknowns.append(value)
            columnnumber += 1
            
        flat_list = [item for sublist in unknowns for item in sublist]

        my_dict = {i:flat_list.count(i) for i in flat_list}

        list_of_key = list(my_dict.keys())
        list_of_value = list(my_dict.values())
                
        thiscounter = 0
        for i in list_of_value:
            # value is the number which we will be replacing with        
            value = list_of_key[thiscounter]
            # i is the number of duplicates = if 1 can replace it
            if i == 1:
                index = 0
                for lists in unknowns:
                    try:
                        if value in lists:
                            unknowns[index] = value
                    except TypeError:
                        index += 1
                        continue

                    index += 1
                    
            thiscounter += 1
            
                # now have unknowns = [1,[2,9], [2,9]]

        unknowncolumnnumber = 0
        unknowncounter = 0
        for x in row:
            
            
            if x == 0:
                if type(unknowns[unknowncounter]) == int:
                    grid[rownumber][unknowncolumnnumber] = unknowns[unknowncounter]
                unknowncounter += 1
            unknowncolumnnumber += 1 


                
        
        rownumber += 1
    
    return grid

grid = [[0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 9, 0, 0, 6, 0, 7],
        [0, 9, 0, 0, 8, 3, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 3, 0, 0, 0, 2, 0],
        [9, 0, 0, 0, 7, 1, 0, 0, 5],
        [0, 0, 5, 1, 0, 2, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 7, 0, 4, 0, 0, 8]]



counter = 0
while any(0 in sl for sl in grid) == True:
    grid = solving_iteration(grid)
    
    if counter == 10:
        break
    
    counter += 1
    print(counter)

grid = finding_singles(grid)

while any(0 in sl for sl in grid) == True:
    grid = solving_iteration(grid)
    
    if counter == 17:
        break
    
    counter += 1
    print(counter)

grid = finding_singles(grid)

while any(0 in sl for sl in grid) == True:
    grid = solving_iteration(grid)
    
    if counter == 17:
        break
    
    counter += 1
    print(counter)

for row in grid:
    print(row)
