from agent import Agent

def log(massage):
    f=open("log.txt","a")
    f.write(massage +"\n")
    f.close()

agents=[
    Agent("PII Agent", 0.02),
    Agent("Cost Agent",0.09),
]

for a in agents:
    if a.check():
        log(a.name + "-Ok-Send ")
    else:
        log(a.name+ "- Too costly-stop")
f=open("log.txt","r")
print(f.read())
f.close()