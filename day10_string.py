# Theory of Strings in Python
# A string is a sequence of characters enclosed in quotes.
# Python strings are immutable, which means their contents cannot be changed after creation.
# Strings support indexing, slicing, concatenation, and many built-in methods.

# Example
name=" Resume.pdf "
print(name)
print(name.strip())
print(name.strip().lower())
print(name.strip().lower().replace(".pdf",".txt"))
print(name.strip().upper())

## Task
e_mail=" MAHEK@GMAIL.COM "
print(e_mail)
print(e_mail.strip())
print(e_mail.strip().lower())
print(e_mail.strip().replace("MAHEK","*****").lower())
