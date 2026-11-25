def check_pii(text):
    if "@" in text:
        return "PII Found"
    else:
        return "Safe send "
files=[
    "Hello world",
    "Email me at a@test.com",
    "No email here",
    "contact b@test.com now"
]
for f in files:
    print(f,"--->",check_pii(f))