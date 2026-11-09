"""Loop Theory

A loop is a control structure that repeats a block of code multiple times.
It is useful when we need to do the same task again and again.

There are mainly two types of loops in Python:
1. for loop -> used when we know how many times to repeat
2. while loop -> used when we repeat until a condition becomes false

Loop components:
- initialization (start value)
- condition (when the loop should continue)
- update/change (so the loop can end)
- body (code executed inside the loop)

Common loop control statements:
- break: stops the loop immediately
- continue: skips the current iteration and continues next
- pass: does nothing, used as placeholder
"""
#EXample

files=["resume.pdf","report.pdf","notes.pdf"]
for file in files:
    print("Checking",file)

## Task
costs=[0.05,0.10,0.03]
for cost in costs:
    if cost > 0.05:
        print(cost,"Too costly stop")
    else:
        print(cost,"Ok -Send")

