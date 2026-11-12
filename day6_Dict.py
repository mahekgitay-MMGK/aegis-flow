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
