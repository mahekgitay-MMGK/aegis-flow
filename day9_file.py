"""Theory of reading files in Python.

File reading brings data stored on disk into a program. Opening a file in read
mode (``r``) creates a stream for accessing its contents; read mode is the
default and normally requires the file to exist. Text mode converts bytes to
characters using an encoding, while binary mode (``rb``) returns raw bytes.

As data is read, the stream's position moves forward. ``read`` gets some or all
remaining content, ``readline`` gets one line, and iterating over the stream
processes it line by line. A ``with`` context manager closes the file when the
block ends, even if an error occurs. Common problems include a missing file,
insufficient permissions, or a decoding error caused by the wrong encoding.
"""
# Example write
'''f=open("aegis_result.txt","w")
f.write("resume.pfd - cost 0.03 - Done")
f.close()
# Example of read
f=open("aegis_result.txt","r")
data=f.read()
print(data)
f.close()
'''
## Task
'''f=open("my_files.txt","w")
f.write("notes.pfd - cost 0.10 - Done")
f.close()

f=open("my_files.txt","r")
data=f.read()
print(data)
f.close()'''

### mini project

project_name=("aegis-Flow")
print(project_name)

f=open("hostory.txt","w")
f.write("resume.pdf - cost 0.03 -Done\n")
f.write("notes.pdf - cost 0.10 -Done\n")
f.close()

f=open("hostory.txt","r")
data=f.read()
print("Aegis-Flow History:")

print(data)
f.close()