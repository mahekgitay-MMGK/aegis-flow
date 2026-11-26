import hashlib 
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
files=["a","b","a","c","b","a"]
seen=[]
count=0
safe_count=0
for f in files:
    h=make_hash(f)
    if h in seen:
        print(f,"--> Duplicate")
        count=count+1
    else:
        seen.append(h)
        print(f,"--->New")

        safe_count=safe_count+1
print("count:",count,"Duplicate")
print("safe count",safe_count, "safe")