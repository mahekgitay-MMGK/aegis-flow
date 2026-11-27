"""Theory: File handling in Python

File handling allows a program to store information in files and retrieve it
later. A typical workflow is to open a file, read from or write to it, and
close it. Prefer the ``with`` statement: it closes the file automatically
when the block ends, even if an error occurs.

	with open("notes.txt", "r", encoding="utf-8") as file:
		contents = file.read()

Common file modes:
	"r"  Read an existing file (the default).
	"w"  Write; create a file or replace its existing contents.
	"a"  Append to the end of a file, creating it if needed.
	"x"  Create a new file, failing if it already exists.
	"b"  Binary mode, for non-text data such as images.
	"+"  Allow reading and writing (for example, "r+").

Use ``read()`` to read all content, ``readline()`` to read one line, or
iterate over the file to process it line by line. Use ``write()`` for a
string and ``writelines()`` for multiple strings; ``writelines()`` does not
add newline characters automatically. Specify an encoding such as UTF-8 for
text files.

The ``pathlib`` module provides convenient, platform-independent path
operations. File operations can fail, so handle relevant exceptions such as
``FileNotFoundError`` and ``PermissionError`` when appropriate. For large
files, process data line by line or in chunks instead of loading everything
into memory at once.
"""

# example

def check_pii(text):
    if "@" in text:
        return " Email PII found"
    elif "0987654321" in  text:
        return "Phone PII found"
    else:
        return "Safe"

f=open("day21_test.txt","w")
f.write("Hi\n")
f.write("a@test.com\n")
f.write("Hello\n")
f.close()

f=open("day21_test.txt","r")
lines=f.readlines()
f.close()

print("lines: ",lines)

for line in lines:
    line=line.strip()
    result=check_pii(line)
    print(line,"----->",result)

print("\n\n\n\n\n\n\n\n")
#tasks

def check_pii(text):
    if "@" in text:
        return "Email PII found"
    elif "1234567890" in text:
        return "Phone PII found"
    else:
        return "safe"

f=open("day21_task.txt","w")
f.write("Hi\n")
f.write("b@text.com\n")
f.write("1234567890\n")
f.write("Bye\n")
f.close()

f=open("day21_task.txt","r")
lines=f.readlines()
f.close()

for line in lines:
    line=line.strip()
    result=check_pii(line)
    print(line,"---->",result)
print("\n\n\n\n\n\n\n\n")

import hashlib
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def check_pii(text):
    if "@" in text:
        return "Email PII FOUND"
    elif "1234567890" in text:
        return "Phone PII found"
    else:
        return "safe"

f=open("day21_miniProject.txt","w")
f.write("Hello\n")
f.write("a@test.com\n")
f.write("Hello\n")
f.write("1234567890\n")
f.write("1990\n")
f.close()

f=open("day21_miniProject.txt","r")
lines=f.readlines()
f.close()
seen=[]
total_spend=0
total_save=0

for line in lines:
    line=line.strip()
    h=make_hash(line)

    if h in seen:
        print(line,"Duplicate skip save 0.05")
        total_save=total_save+0.05
    else:
        seen.append(h)
        result=check_pii(line)
        print(line,"New spend 0.05",result)
        total_spend=total_spend+0.05
print("Total spend",round(total_spend,2))
print("Total save",round(total_save,2))