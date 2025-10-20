# Basic list examples
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_data = ["hello", 42, True, 3.14]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed data:", mixed_data)

# Lists are ordered and changeable
print(f"First fruit: {fruits[0]}")
fruits[0] = "orange"
print(f"Updated fruits: {fruits}")

""" 
*Access Operations*

Indexing: list[0], list[-1]
Slicing: list[1:3], list[:5]
Searching: item in list, list.index(item)
Modification Operations:

Adding: append(), insert(), extend()
Removing: remove(), pop(), del
Changing: list[index] = new_value
Information Operations:

Length: len(list)
Counting: list.count(item)
Sorting: sort(), sorted()
"""