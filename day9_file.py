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
