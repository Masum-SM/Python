import numpy as np

array_1D = np.array([1,2,3,4,5,6])
# print(array_1D) # [1 2 3 4 5 6]

array_2D = np.array([[2,3],[4,5],[6,7]])
# print(array_2D)
"""
[[2 3]
 [4 5]
 [6 7]]
"""
array_3D = np.array([
        [[2,3],[4,5],[6,7]],
        [[2,3],[4,5],[6,7]],
        [[2,3],[4,5],[6,7]]
        ])
# print(array_3D)
"""
[[[2 3]
  [4 5]
  [6 7]]

 [[2 3]
  [4 5]
  [6 7]]

 [[2 3]
  [4 5]
  [6 7]]]
"""

change_1D_to_2D = array_1D.reshape(3,2)
print(change_1D_to_2D)
print()

flip_position = np.flip(change_1D_to_2D)
print(flip_position)
print()


add_array = change_1D_to_2D + flip_position
print(add_array)
print()


mul_array = change_1D_to_2D * flip_position
print(mul_array)
print()

Changed_2D_to_1D = mul_array.flatten()
print(Changed_2D_to_1D)
print()

sum_form_2D = Changed_2D_to_1D.sum()
print(sum_form_2D)
print()

max_in_array = Changed_2D_to_1D.max()
print(max_in_array)
print()

print(array_3D.ndim) #check diamension ans is 3
print(array_3D.size) # total element in array ans is 18
print(array_3D.shape) # shape or formate of array ans is (3, 3, 2)
print(array_3D.dtype) #check type ans is int32

print(Changed_2D_to_1D) # ans [ 6 10 12 12 10  6]
chage_type = Changed_2D_to_1D.astype('f')
print(chage_type.dtype) #check type ans is float32
print(Changed_2D_to_1D) #[ 6 10 12 12 10  6]
print(chage_type) #[ 6. 10. 12. 12. 10.  6.]
make_copy = np.copy(Changed_2D_to_1D)
print(make_copy) #[ 6 10 12 12 10  6]

unsorted = [7,2,6,4,5,8,10]
sorted_arr = np.sort(unsorted)
print(sorted_arr) #[ 2  4  5  6  7  8 10]