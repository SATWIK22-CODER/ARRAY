📘 Project Title: Python Array Manipulation
🧾 Description
This Python script demonstrates basic operations on an array using the built-in array module. It showcases how to:
- Create an array of integers
- Insert an element at a specific index
- Remove an element from the array
- Convert the array to a list and print it
These operations are useful for understanding how arrays work in Python and how they differ from lists in terms of type constraints and performance.

📥 Input
The array is initialized with the following integers:
[1, 2, 3, 4, 5]
Then, the script performs:
- Insertion of 99 at index 3
- Removal of 99 from the array

📤 Output
[1, 2, 3, 99, 4, 5]
After removing 99: <module 'array' from '...'>
print("After removing 99:", arr.tolist())
import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Insert 99 at index 3
arr.insert(3, 99)

# Print array as list
print(arr.tolist())  # Output: [1, 2, 3, 99, 4, 5]

# Remove the first occurrence of 99
arr.remove(99)

# Print array after removal
print("After removing 99:", arr.tolist())  # Output: [1, 2, 3, 4, 5]






