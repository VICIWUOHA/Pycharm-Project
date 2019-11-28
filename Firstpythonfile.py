import numpy as py
print(py.array([1, 2]))
my_list = [1, 2, 3, 4]
my_list2 = [5, 6, 7, 8]
# my_array1 = py.array(my_list)
my_array = py.array([my_list, my_list2])

print(my_array)
print(my_array.shape)

# type of dataset

print(my_array.dtype)

new_array1 = py.zeros(6)
new_array2 = py.ones([6, 6])
new_array3 = py.empty(5)
new_array4 = py.eye(5)
new_array5 = py.arange(1, 50, 5)
print(new_array1)
print(new_array2)
print(new_array3)
print(new_array4)
print(new_array5)
