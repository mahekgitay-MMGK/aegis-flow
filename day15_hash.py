"""Clean notes on hashing.

Hashing maps a value to an integer using a hash function. Dictionaries and
sets use hashes to locate values efficiently. If hashes collide, equality
checks distinguish the values; equal objects must have equal hashes.

Dictionary keys and set members must be hashable. Immutable values such as
strings and integers are hashable; lists and dictionaries are not. Python's
hash values are not guaranteed to stay the same between program runs, so
they should not be used as permanent identifiers.
"""


