count=0
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
    else:
        print("safe")

print(f,"-->","count;",count)