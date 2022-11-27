import numpy as np

py_list = [1,2,3,4,5]
print(py_list) #[1, 2, 3, 4, 5]

num_array = np.array([9,8,7,6,5]) #give an array which vale serial memory location in memory address.
print(num_array) #[9 8 7 6 5]

num_10_zero = np.zeros(10) #provides zeros
print(num_10_zero) #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

num_10_ones = np.ones(10) #provides ones
print(num_10_ones) #[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

num_sequence = np.arange(15)  #provide 0 to 14 number in sequence
print(num_sequence) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

num_stpper = np.arange(0 ,30 ,5) # give number 0 t0 30 after 5 value
print(num_stpper) #[ 0  5 10 15 20 25]

num_spaced = np.linspace(0,20,5)
print(num_spaced) #[ 0.  5. 10. 15. 20.]