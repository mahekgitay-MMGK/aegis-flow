def check_pii(text):
    if "98765" in text:
        return "Phone PII"
    else:
        return " No phone PII safe"

files=[
    "Hello",
    "call 98765",
    "No phone"

]
for f in files:
    print(f , "----> ",check_pii(f))