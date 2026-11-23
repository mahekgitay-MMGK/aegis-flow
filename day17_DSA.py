import hashlib , json
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
def log(massage):
    f=open("day17_DSAlog.txt","a")
    f.write(massage + "\n")
    f.close()
files=["a","a","b","b","b","c"]
seen=[]
total_spend=0
total_save=0

f=open("day17_DSAlog.txt","r")
print(f.read())
f.close()
for f in files:
    h=make_hash(f)
    if h in seen:
        print("DUPLICATE - SKIP - SAVE 0.05")
        total_save=total_save+ 0.05
        
        log("DUPLICATE - SKIP - SAVE  0.05")
    else:
        seen.append(h)
        print("NEW - SEND -SPEND 0.05")
        total_spend=total_spend+ 0.05
        
        log("NEW - SEND -spend 0.05")
print("Total spend :",total_spend)
print("Totral save",total_save)

log(f"Total spend:{total_spend} - Total save: {total_save} ")

report={"total_soend": total_spend,"total_save":total_save}
f=open("day17_report.json","w")
json.dump(report,f)
f.close()
f=open("day17_report.json","r")
print(f.read())
f.close()