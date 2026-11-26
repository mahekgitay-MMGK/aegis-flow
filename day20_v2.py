import hashlib,re
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()
def check_pii(text):
    email_pattern=r"[a-z]+@[a-z]+\.[a-z]+"
    phone_pattern=r"\d{10}"
    if re.search(email_pattern,text):
        return "Email PII FOUND"
    elif re.search(phone_pattern,text):
        return "Phone PIII FOUND"
    else:
        return "safe You can send"

files=["hello","a@test.com","hello","9187654320"]
seen=[]
for f in files:
    h=make_hash(f)
    if h in seen:
        print(f,"---> Dublicate -- skip")
    else:
        seen.append(h)
        print(f,"---> New-",check_pii(f),"safe send")