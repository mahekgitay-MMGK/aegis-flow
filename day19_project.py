import re 

def check_Pii(text):
    email_pattern=r"[a-z]+@[a-z]+\.[a-z]+"
    phone_pattern=r"\d{10}"
    if re.search(email_pattern,text):
        return "Email PII found - HIDE"
    elif re.search(phone_pattern,text):
        return "Phone PII found - HIDE"
    else:
        return "safe"
files=[
    "Mail is z@y.com",
    "call 1111111111",
    "hello"
]
for f in files:
    print(f,"----->",check_Pii(f))