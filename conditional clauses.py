import numpy as np

a = np.array([100, 400, 500, 600])  # each member as x
b = np.array([10, 15, 20, 25])  # each member as y
condition = np.array([True, True, False, False])

# using loops
c = [x if cond else y for x, cond, y in zip(a, condition, b)]
print(c)

# we have to use a loop - np.where which has 3args (condition, value for true, value for false)
c2 = np.where(condition, a, b)
print(c2)
# where the value of x is>200, we return 0, else, we return 1
c3 = np.where(a > 200, 0, 1)
print(c3)

# Standard functions of arrays
# sum of array

print(a.sum())

d = np.array([[1, 2], [3, 4]])
print(d)
print(d.sum(0))
print(d.sum(1))

# mean
print('statistical values of a are')
print(a.mean())
print(a.std())
print(a.var())

condition2 = np.array([True, False, True])
print(condition2.any())
print(condition2.all())

new_array = np.array([1, 10, 4, 8, 2, 5])
new_array.sort()
print(new_array)

# unique arrays

arr3 = np.array(['solid', 'liquid', 'solid', 'gas', 'gas', 'liquid', 'aqueous'])

print(np.unique(arr3))

arr3.sort()

print(np.in1d(['aqueous', 'first', 'gas'], arr3))
