import re
count=0
safe_count=0
def check_pii(text):
    global count,safe_count
    emial_pattern=r"[a-z]+@[a-z]+\.[a-z]+"
    phone_pattern=r"\d{10}"
    if re.search(emial_pattern,text):
        count=count+1
        return "PII Email FOUND "
    elif re.search(phone_pattern,text):
        count=count+1
        return "PII PHONE FOUND"
    else:
        safe_count=safe_count+1
        return "SAFE"

files=[
    "Hello world",
        "Mail me a@test.com",
        "call 9807654321",
        "hi @",
        "Mail is z@y.com",
        "call 1111111111",
        "hello",
]
for f in files:
    print(f"{f},---->,{check_pii(f)},\ncount:{count},\nsafe count: {safe_count}")