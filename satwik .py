import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])
arr.insert(3, 99)  # Insert 99 at index 2
print(arr.tolist())  # Output: [1, 2, 99, 3, 4, 5]
arr.remove(99)  # Removes the first occurrence of 25
print("After removing 25:", array)