import numpy as np
arr = np.arange(12)
print(arr)

np.save('saved_array', arr)
# saving a new array to a file
my_new_array = np.load('saved_array.npy')
print(my_new_array)

# saving multiple arrays

arr_1 = np.arange(20)
arr_2 = np.arange(40)

np.savez('saved_archive.npz', x=arr_1, y=arr_2)
load_archive = np.load('saved_archive.npz')

print('load_archive[x] is')
print(load_archive['x'])
print('while loaded_archive[y] is')
print(load_archive['y'])

# saving to text file

np.savetxt('txtfile.txt', arr_1, delimiter=',')

# loading of txt files

load_txt_file = np.loadtxt('txtfile.txt', delimiter=',')

print('load_txt_file is')
print(load_txt_file)
