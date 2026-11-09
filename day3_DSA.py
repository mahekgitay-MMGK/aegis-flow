"Here we start solve DSA prooblems"
costs=[0.05,0.10,0.03,0.20]
count=0
for cost in costs:
    if cost > 0.05:
        count=count +1
print("Too costly count: ",count)