files=[
    {"file": "resume.pdf", "cost" : 0.03},
    {"file": "b.pdf"},
    {"file": "notes.pdf", "cost" : 0.10}
]

total= 0
for f in files:
    try:
        total = total + f["cost"]
    except:
        print(f["file"],"No cost - skip - add 0")
print("total cost:",total)