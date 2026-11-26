import hashlib,re
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
def check_pii(text):
    email_pattern=r"[a-z]+@[a-z]+\.[a-z]+"
    phone_pattern=r"\d{10}"
    if re.search(email_pattern,text):
        return "Email PII Found"
    elif re.search(phone_pattern,text):
        return "phone PII FPOUND"
    else:
        return "Safe"
def log(massage):
    f=open("day20_aegisFlow.txt","a")
    f.write(massage + "\n")
    f.close()
files=[
    "hello",
    "a@test.com",
    "b@test.com",
    "call 9008",
    "call 1234567890",
    "b@test.com",
    "hello"
]
seen=[]
total_spend=0
total_save=0
for f in files:
    h=make_hash(f)
    if h in seen:
        print(f,"---> duplicate file skip- save - 0.05")
        total_save=total_save+0.05
        log(f" file:{f}-- duplicate,save cost: {total_save}")
    else:
        seen.append(h)
        result=check_pii(f)
        total_spend=total_spend+0.05
        print(f,"New -",result,"spend 0.05")
        log(f"file: {f} -- new, spend cost: {total_spend}")
print("Total spend",total_spend)
print("Total save",total_save)