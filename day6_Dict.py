"""Theory of Python dictionaries (dicts).

A dictionary is a mutable collection of key-value pairs. A key is used to
retrieve its corresponding value, much like looking up a word in a glossary.

Important properties:
- Keys are unique and must be hashable, such as strings, numbers, or tuples
	containing only hashable values.
- Values can be any Python object.
- Dictionaries preserve insertion order. Updating an existing key replaces
	its value without creating a duplicate key.
- Dictionary lookup, insertion, and deletion are typically efficient.

Common operations:

		person = {"name": "Ava", "age": 16}  # Create
		person["age"] = 17                    # Update
		person["city"] = "Seattle"            # Add
		name = person["name"]                  # Access (raises KeyError if absent)
		age = person.get("age")                # Safe access (None if absent)
		"name" in person                       # Check whether a key exists
		del person["city"]                     # Remove a pair

Use ``keys()``, ``values()``, and ``items()`` to access keys, values, and
key-value pairs when iterating over a dictionary.
"""
#Task

"""student_data = [
	{"Name": "Mahek", "Age": 18, "Marks": 90, "Grade": "A++"},
	{"Name": "Riya", "Age": 16, "Marks": 77, "Grade": "B"},
	{"Name": "Meck", "Age": 17, "Marks": 42, "Grade": "E"},
	{"Name": "Reem", "Age": 20, "Marks": 60, "Grade": "C"},
	{"Name": "Neha", "Age": 19, "Marks": 80, "Grade": "A"},
]
print(student_data)
"""

## Example
"""file_info={"file": 'resume.pdf', 'cost' :0.05}
print(file_info)
print("file: ", file_info["file"])
print("cost: ", file_info["cost"])

file_info["is_duplicate"]=False
print(file_info)
"""
### Task
agent_info={"name" : "Data Analyst Agent", "cost": 0.10,"is_live" : False}
print(agent_info)
print(agent_info["name"])
agent_info["file"] = 100
print(agent_info)
