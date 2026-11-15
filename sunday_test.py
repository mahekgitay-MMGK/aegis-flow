print("Aegis-Flow")
cost=0.10

if cost > 0.05:
    print("Too high")
else:
    print("ok")

files=["a.pdf","b.pdf"]
for file in files:
    print("file",file)

try:
    file={"file": "a.pdf","cost": 0.03}
    print(file["hash"])
except:
    print("no hash")

total=0
while total <0.10:
    total=total + 0.03
print(total) 