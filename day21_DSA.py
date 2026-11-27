import hashlib
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

f=open("day21_DSA.txt","w")
f.write("a\n")
f.write("b\n")
f.write("a\n")
f.write("c\n")
f.write("b\n")
f.close()
seen=[]
count=0
safe_count=0
f=open("day21_DSA.txt","r")
lines=f.readlines()
f.close()

for line in lines:
    line=line.strip()
    h= make_hash(line)
    if h in seen:
        print(line,"--->Duplicate ")
        count=count+1
    else:
        seen.append(h)
        print(line,"---> safe")
        safe_count=safe_count+1
print("count",count)
print("safe count",safe_count)