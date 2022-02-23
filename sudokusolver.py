def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

def making_grid(l, n):
    print(l)


grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

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
