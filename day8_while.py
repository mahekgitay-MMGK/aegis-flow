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