import hashlib, re
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
def check_pii(text):
    email_pattern=r"[a-z]+@[a-z]+\.[a-z]+"
    phone_pattern=r"\d{10}"
    if re.search(email_pattern,text):
        return "Email PII found"
    elif re.search(phone_pattern,text):
        return "Phone PII Found"
    else:
        return "safe"

def log(massage):
    f=open("day20_log.txt","a")
    f.write(massage + "\n")
    f.close()


files=[
    "hello","a@test.com","hello","2134567890"
]
seen=[]
total_spend=0
total_save=0
for f in files:
    h=make_hash(f)
    if h in seen:
        print(f,"---> Duplicate Skip -- Save 0.05")
        total_save=total_save+0.05
        log(f"Duplicate files: {f} - save 0.05")
    else:
        seen.append(h)
        result=check_pii(f)
        print(f,"---> New",result,"-spend 0.05")
        total_spend=total_spend+0.05
        log(f"New {f}-{result}-spend 0.05")

print("total spend:",total_spend)
print("total save: ",total_save)