costs=[0.03,0.05,0.10,0.20,0.50]

max_cost=costs[0]
for cost in costs:
    if cost > max_cost:
        max_cost= cost

print(" Max costs: ",max_cost)