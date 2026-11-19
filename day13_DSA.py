from agent import Agent
a1=Agent("a1",0.02)
print(a1.name,a1.check())
a2=Agent("a2",0.08)
print(a2.name,a2.check())
a3=Agent("a3",0.03)
print(a3.name,a3.check())
a4=Agent("a4",0.10)
print(a4.name,a4.check())
count=0
if a1.check():count=count+1
if a2.check():count=count+1
if a3.check():count=count+1
if a4.check():count=count+1
print(count)

cheapest=a1
if a2.cost < cheapest.cost:
    cheapest=a2
if a3.cost < cheapest.cost:
    cheapest=a3
if a4.cost < cheapest.cost:
    cheapest=a4
print("Cheap value",cheapest.name,cheapest.cost)