"""JSON (JavaScript Object Notation) — basic theory

JSON is a text-based format for storing and exchanging structured data. It is
language-independent, lightweight, and commonly used by APIs and configuration
files. Although its name refers to JavaScript, JSON can be read and written in
many programming languages.

JSON values and their Python equivalents:
		JSON object  {"name": "Ava"}    -> dict
		JSON array   ["red", "blue"]    -> list
		JSON string  "hello"            -> str
		JSON number  42 or 3.5           -> int or float
		JSON boolean true or false       -> True or False
		JSON null    null                -> None

An object contains key/value pairs. Keys must be strings and are written in
double quotes. Arrays contain ordered values. Objects and arrays may be nested.
JSON does not support comments, trailing commas, or values such as tuples,
sets, and Python's None/True/False spellings.

Example of valid JSON:
		{
			"student": {"name": "Ava", "active": true},
			"scores": [92, 87],
			"note": null
		}

In Python, the built-in ``json`` module converts between JSON text and Python
data: ``json.loads(text)`` parses a string, ``json.load(file)`` reads a file,
``json.dumps(value)`` creates a JSON string, and ``json.dump(value, file)``
writes JSON to a file. Parsing invalid JSON raises ``json.JSONDecodeError``.
"""
import json

data={"file":"resume.pdf", "cost":0.03}

#write Dict to json file
f=open("data.json","w")
json.dump(data,f)
f.close()

#Read json file
f=open("data.json","r")
new_data=json.load(f)
print(new_data)
print("file: ",new_data["file"])
f.close()