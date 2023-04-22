import numpy as np

A1 = np.array([11, 33, 22, 44, 66, 55])
A2 = np.array([10, 30, 20, 40, 60, 50])

# 1. Extract elements of A1 from index 2 to 5
extracted_A1 = A1[2:6]
print(extracted_A1)

# 2. Reshape A1 into a (3, 2) array
reshaped_A1 = np.reshape(A1, (3, 2))
print(reshaped_A1)

# 3. Join A1 and A2
joined_arrays = np.concatenate((A1, A2))
print(joined_arrays)

# 4. Split A1 into 3 arrays
split_A1 = np.array_split(A1, 3)
print(split_A1)

# 5. Search for the number 44 in A1
if np.isin(44, A1):
  print("44 is in A1")
else:
  print("44 is not in A1")

# 6. Print all even numbers of A1
even_numbers = A1[np.where(A1 % 2 == 0)]
print(even_numbers)

# 7. Sort A2
sorted_A2 = np.sort(A2)
print(sorted_A2)

# 8. Filter the odd numbers in A1
odd_numbers = filter(lambda x: x % 2 != 0, A1)
print(list(odd_numbers))
