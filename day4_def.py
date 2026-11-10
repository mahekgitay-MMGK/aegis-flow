"""Theory: Python functions and the ``def`` keyword.

Functions are named, reusable blocks of code. The ``def`` keyword creates a
function. The function body is indented and runs when the function is called.

Syntax:
	def function_name(parameters):
		statements
		return value

Parameters are names listed in the definition; arguments are the values
passed in a call. ``return`` sends a result back to the caller. A function
without an explicit ``return`` returns ``None``. Parameters can have default
values, and arguments can be passed by position or by keyword. Names created
inside a function are usually local to that function.
"""

# Example
def is_too_costly(cost):
    return cost > 0.05

print(is_too_costly(0.10))
print(is_too_costly(0.03))


## Task
def check_duplicate(is_duplicate):

    
    if is_duplicate == True:
        return"Duplicate - skip"
    else:
        return "New file - send"

    

print(check_duplicate(False))
print(check_duplicate(True))
    
### Project

project_name=("Aegis Flow")
print(project_name)

def check_duplicate(is_duplicate):
    if is_duplicate== True:
        return "Duplicate file"
    else:
        return "New file - send "

def too_costly(cost):
    return cost >= 0.05

print(check_duplicate(True))
print(check_duplicate(False))
print(too_costly(0.10))
print(too_costly(0.20))
print(too_costly(0.03))
print(too_costly(0.05))

#### Interviwe Question
"""
def is make your own fuction. makme once use thousand of times.
example: if male one def called too_cosly(cost):
                                return cost > 0.05
                                then we called fuction too costly(0.10) it's give you true
"""