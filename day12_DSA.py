
class Agent:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
        

    def check(self):
        
        if self.cost <= 0.05:
            return True
            
        else:
            return False
a1=Agent("a1",0.03)
a2=Agent("a2",0.10)
a3=Agent("a3",0.02)

count=0
if a1.check():count=count+1
if a2.check():count=count+1
if a3.check():count=count+1
print (count)