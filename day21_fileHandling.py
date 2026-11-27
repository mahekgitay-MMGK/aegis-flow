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
