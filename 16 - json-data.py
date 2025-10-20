import json

# Convert Python data to JSON
data = {
    "name": "Leandro Gois",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"],
    "active": True,
    "salary": None
}

json_string = json.dumps(data)
print("JSON string:")
print(json_string)

# Convert JSON back to Python
parsed_data = json.loads(json_string)
print("\nParsed Python data:")
print(parsed_data)

# Accessing data from the parsed JSON
print(f"\nName: {parsed_data['name']}")
print(f"Skills: {', '.join(parsed_data['skills'])}")

# Writing JSON data to a file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
# Reading JSON data from a file
with open('data.json', 'r') as json_file:
    file_data = json.load(json_file)
print("\nData read from file:")
print(file_data)