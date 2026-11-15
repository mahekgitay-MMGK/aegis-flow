f=open("dsa.txt","w")
f.write("a.pdf - cost 0.03")
f.close()

f=open("dsa.txt","r")
data=f.read()
print("data: ",data)
f.close()
print("problem DSA 1")