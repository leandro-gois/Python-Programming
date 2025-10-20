# Basic dictionary example
student = {
    'name': 'Leandro',
    'age': 20,
    'grade': 'A',
    'courses': ['Math', 'Science']
}

print("Student info:", student)
print("Student name:", student['name'])

""" 
*Core Dictionary Operations*
Accessing: dict[key]
Adding/Updating: dict[key] = value
Removing: del dict[key], dict.pop(key)
Length: len(dict)
Keys: dict.keys()
Values: dict.values()
Items: dict.items()
Checking Existence: key in dict
Iteration: for key in dict, for key, value in dict.items()
"""
