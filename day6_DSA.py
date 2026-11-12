files=[
    {"files":"resume.pdf","cost": 0.03, "is_duplicate": False},
    {"files":"notes.pdf","cost": 0.10, "is_duplicate": False},

    {"files":"student.pdf","cost": 0.40, "is_duplicate": False}
]

count=0

for f in files:
    if f["cost"] > 0.05:
        count=count+1
print("Too costly count: ", count)