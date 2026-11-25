import re

count = 0
safe_count = 0

def check_pii(text):
    global count,safe_count

    email_pattern = r"[a-z]+@[a-z]+\.[a-z]+"
    phone_pattern = r"\d{10}"

    if re.search(email_pattern, text):
        count =count +1
        return "Email PII FOUND"
    elif re.search(phone_pattern, text):
        count=count+1
        return "Phone PII found"
    else:
        safe_count =safe_count+ 1
        return "safe"
files=[
    "a@test.com","hello @","b@test.com","Hi","c@test.com","Phone 11","call 0987654321"
]
for f in files:
    print(f,"------>",check_pii(f))
    print("count:",count)
    print("safe count :",safe_count)
