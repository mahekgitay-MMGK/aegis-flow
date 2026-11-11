"""Python list theory

A list is an ordered, mutable collection that can hold values of different
types. Lists allow duplicate values and use zero-based indexing.

Lists are commonly represented as dynamic arrays: elements occupy consecutive
positions, and the list can grow or shrink as items are added or removed.
Indexing and replacing an item by index are typically O(1). Searching by value,
inserting in the middle, or removing from the middle is typically O(n), because
elements may need to be inspected or shifted. Appending is amortized O(1).

Slices describe ranges and produce a new list. Assignment through an index or
slice can change a list. A list variable refers to a list object; assigning that
reference to another variable does not copy the list. A shallow copy duplicates
the outer list but still shares any nested mutable objects.

Lists are useful when order matters and the collection needs to change. Tuples
are preferable for fixed collections, while sets are designed for unique
elements and fast membership checks. A list comprehension is a concise way to
describe a new list derived from an iterable.
"""
# Example
'''files=["report.pdf","docoment.pdf","resume.pdf","student.pdf"]

print(files)
print("Total files",len(files))
files.append("notes.pdf")
files.extend(["report.pdf"])
files.remove("docoment.pdf")

print(files)
print("Total files now: ",len(files))'''

## Task

costs=[0.03,0.05,0.10,0.20,0.50]
print("Total cost: ",len(costs))

costs.append(0.40)
print(costs)
costs.remove(0.03)
print(costs)
print("Now total cost: ",len(costs))