# Basic function definition and usage
def greet_user(name):
    """Say hello to a user"""
    return f"Hello, {name}! Welcome to Python!"

# Call the function
message = greet_user("Leandro")
print(message)

# Call it multiple times
print(greet_user("Bob"))
print(greet_user("Charlie"))

anonymous_function = lambda x: f"Hi, {x}!"
print(anonymous_function("Dana"))