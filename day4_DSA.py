costs=[0.10,0.3,0.20,0.30,0.05]

def is_too_costly(cost):
    return cost > 0.05

count=0
for cost in costs:
    if is_too_costly(cost):
        count= count + 1

print("Too costly count:", count)