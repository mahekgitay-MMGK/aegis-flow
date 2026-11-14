"""Theory of the while loop

A while loop repeatedly executes a block of code as long as its condition is
true. The condition is checked before each iteration, so the block may not run
at all if the condition is false initially. The loop should make progress
toward a state where its condition becomes false; otherwise, it may run
indefinitely. A while loop is useful when the number of repetitions depends on
a condition rather than a fixed count.
"""
# example

cost=0
while cost < 0.05:
    print("processing... cost",cost)
    cost= cost + 0.03

print("stop - cost limit reched:",cost)

##Task

files_done=0
while files_done <3 :
    print("Processing file number:",files_done)
    files_done = files_done + 1

print(files_done)

### MINI project

project_name="aegis-flow"
print(project_name)
total_cost=0
file_count=0

while total_cost < 0.10:
    print("Adding file , cost:",total_cost)
    total_cost= total_cost +0.03
    file_count=file_count +1

print("Total file added: ",file_count)
print("Final cost:",total_cost)
print("Stop - cost limit reached")