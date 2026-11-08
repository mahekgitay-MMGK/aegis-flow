"Day 2 if else statmentt this are very important to take and set multiple conditions"

#Example

is_duplicate=True
total_cost=0.05
if is_duplicate==True:
    print("Duplicate - skip- save")
else:
    print("New file - send to LLM")
    print("Cost: ",total_cost)

## Task

total_cost=0.10
limit=0.05
if total_cost > limit:
    print("Too costly - STOP ")
else:
    print("Ok - send to LLM")

### PROJECT
 
project_name ="aegis-flow"
is_duplicate= False
total_cost=0.03
limit=0.05
print(project_name)

if is_duplicate == True:
    print("Duplicate - skip")
else:
    print("New File- Check cost")
if total_cost > limit:
    print("Too costly - stop")
else:
    print("Cost ok-send to LLM ")
    print("cost", total_cost)
