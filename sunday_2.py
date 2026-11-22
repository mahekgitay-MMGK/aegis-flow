from sunday_test2 import Agent
a2=Agent("cost",0.09)
print(a2.check())

def log(massage):
    f=open("log2.txt","a")
    f.write(massage + "\n")
    f.close()
log("Test ok")

f=open("log2.txt","r")
print(f.read())
f.close()

import hashlib

text="hello world"
h1=hashlib.sha256(text.encode()).hexdigest()
print(h1[:10])