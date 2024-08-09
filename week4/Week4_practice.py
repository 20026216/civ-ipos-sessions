my_braincells = [[1,2,3],
                 [4,5,6],
                 [7,8,9]
                 ]

print(my_braincells) # grabs all
print(my_braincells[0]) # grabs 1st rows
print(my_braincells[1])

print(my_braincells[0][0]) # grabs the 1st thing in the 1st row in the 1st column

# grabbing data like this is called random selection

for row in my_braincells: # grabs all of the data sequencially
    for cell in row:
        print(cell, end= " ")
    print()


def make_2d(rows, cols, value=none):
    list_2d =[]
    for _ in range(rows):
        elems = []
        for _ in range(cols):
            elems.append(value)
        list_2d.append(elems)
    return list_2d

brain_list = make_2d(3, 3)

print(brain_list) # makes 2d list of nones depending on the row and column params

def make_2d_refactor(rows, cols, value=None):
    return [[value for _ in range(cols)] for _ in range(rows)]

brain_list2 = make_2d_refactor(3, 3)

print(brain_list2)