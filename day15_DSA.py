import hashlib

def make_check(text):
    return hashlib.sha256(text.encode()).hexdigest() 

files=["a","b","a","c","b","a"]
seen=[]
count=0
for f in files:
    h=make_check(f)
    if h in seen:
        print(f[:12],"Duplicate skip ")
    else:
        print(f[:12],"New file send")
        seen.append(h)
        count += 1
print(count,f)

unique=[]
for f in files:
    if f not in seen:
        seen.append(f)
    
        unique.append(f)
print(unique)
