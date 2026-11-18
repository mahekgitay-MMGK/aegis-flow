"""Theory: Classes in Python

A class is a blueprint for creating objects. It groups data (attributes) and
behavior (methods) into one reusable definition. An object is an instance of a
class, and each instance can hold its own attribute values.

The ``__init__`` method initializes a new instance. Its first parameter,
conventionally named ``self``, refers to that instance. Instance methods use
``self`` to read or update instance attributes. Class attributes are shared by
instances, while instance attributes belong to individual objects.

Classes help organize related code and model concepts. Inheritance lets a
class reuse or extend another class's behavior; encapsulation groups related
state and operations; and polymorphism allows different object types to
respond to the same method call in their own way.
"""
## Example
'''class Agent:
    def __init__(self,name):
        self.name=name
agent1=Agent("Data Analyst Agent")
print(agent1.name)

agent2=Agent("pII Agent")
print(agent2.name)
'''
### Task
'''class File:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
file1 = File("resume.pdf", 0.03)
print(file1.name,file1.cost)

file2= File("notes.pdf",0.10)
print(file2.name,file2.cost)

        '''
### Mini project
class Agent:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost

    def check(self):
        if self.cost > 0.05:
            print(self.name,"Toocostly - stop")
        else:
            print(self.name,"ok - send")

a1=Agent("Data analyst agent",0.03)
a1.check()

a2=Agent("PII Agent",0.10)
a2.check()
    