import hashlib 
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
files=["a","b","a","c","b","a"]
seen=[]
count=0
safe_count=0
total_spend=0
total_save=0
for f in files:
    h=make_hash(f)
    if h in seen:
        print(f,"--> Duplicate")
        count=count+1
        total_save=total_save+0.05
    else:
        seen.append(h)
        print(f,"--->New")

        safe_count=safe_count+1
        total_spend=total_spend+0.05

print("count:",count,"Duplicate")
print("safe count",safe_count, "safe")
print("Total spend",total_spend)
print("Total save",total_save)
