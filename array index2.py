import numpy as np
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
#prints the array index of 2
print(arr2d[2])

# prints the index 1 item of the array with index of 1
print(arr2d[1][1])

# slices of 2d arrays

# prints 1st row with index of zero but first two columns , [0:1], [0:2] means first row, second column
slice1 = arr2d[0:3, 0:1]
# print(slice1)

slice2 = arr2d[0:1, 0:1]
print(slice2)

# replacing values of arrays after slicing
arr2d[:3, 1:] = 15
# print(arr2d)

# using loops
arr_len = arr2d.shape[0]

for i in range(arr_len):
    arr2d[i] = i
print(arr2d[[1, 2]])






