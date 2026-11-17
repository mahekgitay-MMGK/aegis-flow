import json
files=[{"file": "report.docx", "cost": 0.05},
{"file": "photo.jpg", "cost": 0.02},
{"file": "invoice.pdf", "cost": 0.04},
{"file": "notes.txt", "cost": 0.01},
{"file": "presentation.pptx", "cost": 0.08},

]
# write file
f=open("files.json","w")
json.dump(files,f)
f.close()

# read file json
f=open("files.json","r")
new_files=json.load(f)
print(len(new_files))
f.close()
for f in new_files:
    print("file: ",f["file"],"cost: ",f["cost"])
