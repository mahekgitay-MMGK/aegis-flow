"""
Theory of try in Python

The try statement is used to handle exceptions (errors) in Python.
It helps prevent the program from crashing when something unexpected happens.

Syntax:
try:
    # code that may raise an error
except SomeError:
    # code to handle the error
else:
    # runs when there is no error
finally:
    # always runs, whether there is an error or not

Important points:
- The try block contains code that can fail.
- The except block catches the exception and handles it.
- The else block runs only if no exception occurs.
- The finally block always executes, used for cleanup like closing files.

Example:
"""

'''try:
    print(10/0)
except:
    print("Can't divided by zero - App lives")
print("After try- App still  running")'''


## Task
'''files_info={"file": "resume.pdf", "cost" : 0.05}

try:
    print(files_info["hash"]," This key does Not exist - Will error")
except:
    print("No hash key -App lives")

print("After try- App still  running")'''

### MInni pproject

project_name="Aegis Flosw"
print(project_name)

files=[
    {"file": "resume.pdf", "cost" : 0.05},
    {"file": "notes.pdf", "cost" : 0.10}
]
for f in files:
    try:
        print("file: ",f["file"],"cost:",f["cost"],f["hash"])
    except:
        print(f["file"], "No hash- App lives-skip hash")

print("After try- App still  running")