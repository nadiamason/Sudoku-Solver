from collections import Counter
from itertools import chain
from typing import Type

s = [1,2,3,4,5,6,7,8,9]
unknowns = [[1,9],[2,9],[2,9], [3,9]]


# get counts of all the items that are in s and list2
#counts = Counter(word for word in chain.from_iterable(unknowns) if word in s)

#print(counts)

#if 1 in counts.values():
#    print("yes")
    
# create lists filter by count <  3
#newList = [[item for item in sublist if counts.get(item, 0) < 3] for sublist in list2]

flat_list = [item for sublist in unknowns for item in sublist]
print(flat_list)

my_dict = {i:flat_list.count(i) for i in flat_list}
print(my_dict)

list_of_key = list(my_dict.keys())
list_of_value = list(my_dict.values())
 
counter = 0
for i in list_of_value:
    
    value = list_of_key[counter]

    if i == 1:
        index = 0
        for lists in unknowns:
            try:
                if value in lists:
                    unknowns[index] = value
            except TypeError:
                continue

            index += 1
                
    counter += 1
 
print(unknowns)
