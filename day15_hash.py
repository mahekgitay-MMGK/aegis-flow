"""Clean notes on hashing.

Hashing maps a value to an integer using a hash function. Dictionaries and
sets use hashes to locate values efficiently. If hashes collide, equality
checks distinguish the values; equal objects must have equal hashes.

Dictionary keys and set members must be hashable. Immutable values such as
strings and integers are hashable; lists and dictionaries are not. Python's
hash values are not guaranteed to stay the same between program runs, so
they should not be used as permanent identifiers.
"""


import hashlib

text1="resume.pdf content"
text3="notes.pdf content"
text2="resume.pdf content"

h1=hashlib.sha256(text1.encode()).hexdigest()
h2=hashlib.sha256(text2.encode()).hexdigest()
h3=hashlib.sha256(text3.encode()).hexdigest()
print("h1",h1[:10])
print("h2",h2[:10])
print("h3",h3[:10])

if h1==h2:
    print( "h1 and h2 duplicate - skip")
else:
    print( "h1 and h2 new send")
if h1==h3:
    print( "h1 and h3 duplicate - skip")
else:
    print( "h1 and h3 new send")
if h3==h2:
    print( "h3 and h2 duplicate - skip")
else:
    print( "h3 and h2 new - send")