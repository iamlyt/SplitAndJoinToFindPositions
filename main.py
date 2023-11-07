# read numbers from line 1
# read number 'x' from line 2
# print out positions of 'x' (index)

# separate numbers in numbers_list
numbers_list = input().split()
x = input()

# create an empty list to store indices found (or not)
positions = []

# iterate through the numbers of elements in the numbers_list
for index in range(len(numbers_list)):
    # if the element of that index is the same as 'x'
    if numbers_list[index] == x:
        # then add it to the 'positions' list
        positions.append(index)

# checks if list 'positions' is empty, if empty print 'not found'
if not positions:
    print("not found")
# if not empty, print the indices found
else:
    print(*positions)
