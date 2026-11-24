count=0
count_safe=0
files=[
    "Hello",
    "a@test.com",
    "b@test.com",
    "hi"
]
for f in files:
    if "@" in f:
        print("PII found - stop")
        count=count+1
    elif "@" not  in  f:
        count_safe=count_safe+1
        
    else:
        print("safe")
        count_safe=count_safe+1

print("-->","unsafe file",count)
print(" safe count : ",count_safe)
