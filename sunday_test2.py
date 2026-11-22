import json
files={"file":"a.pdf","cost":0.05}
f=open("file.json","w")
json.dump(files,f)
f.close()

f=open("file.json","r")
new_files=json.load(f)
print(new_files)
print("file:",new_files["file"])
f.close()

class Agent:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    def check(self):
        if self.cost <= 0.05:
            return True
        else:
            return False
a1=Agent("PII",0.02)
print(a1.name)

