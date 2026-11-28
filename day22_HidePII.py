"""
Hiding PII (Personally Identifiable Information)

PII is any information that can identify, contact, or locate a person, such as a
name, email address, phone number, national ID, address, or account number.
The purpose of hiding PII is to protect privacy and reduce the risk of identity
theft, unauthorized access, or data misuse.

PII should be minimized by collecting only necessary data, masked or redacted
when full values are not needed, and encrypted when data must be stored or
transmitted. Access should be restricted to authorized users and protected by
logging, retention policies, and secure deletion.

Common hiding methods include masking part of a value, such as showing only the
last four digits of an account number, or replacing sensitive values with
asterisks. Data anonymization removes identifying details, while pseudonymization
replaces identifiers with artificial tokens. Encryption protects PII from
unauthorized viewing when handled securely and with proper key management.

Effective PII protection requires understanding applicable privacy laws and
organizational policies, validating the masking or redaction rules, and ensuring
that sensitive data is not exposed through backups, logs, screenshots, exports,
or error messages.
"""
## Example

import re

def hide_pii(text):
    text=re.sub(r"[a-z]+@[a-z]+\.[a-z]+","***@gmail.com",text)
    text=re.sub(r"\d{10}","**********",text)
    return text
texts=[
    "My email is a@test.com",
    "call me  9876543210",
    "Hello world",
]
for t in texts:
    hidden=hide_pii(t)
    print("Original",t)
    print("Hidden:",hidden)
    print("----")

## Task

print("\n\n\n\n\n\n")
import re

def hide_pii(text):
    text=re.sub(r"[a-z]+@[a-z]+\.[a-z]+","***@gmail.com",text)
    text=re.sub(r"\d{10}","**********",text)
    return text

texts=[
    "x@y.com",
    "1234567890",
    "Hello",
]
for t in texts:
    hidden=hide_pii(t)
    print("Original",t)
    print("Hidden",hidden)
    print("---")

print("\n\n\n\n\n\n")
### mini practice project

import hashlib ,re
def make_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def hide_Pii(text):
    text=re.sub(r"[a-z]+@[a-z]+\.[a-z]+","***@gmail.com",text)
    text=re.sub(r"\d{10}","**********",text)
    return text
def check_pii(text):
    email_pattern=r"[a-z]+@[a-z]+\.[a-z]+"
    phone_pattern=r"\d{10}"
    if re.search(email_pattern,text):
        return "Email PII FOUND"
    elif re.search(phone_pattern,text):
        return "Phone PIII FOUND"
    else:
        return "safe"
f = open("day22_hidePii.txt","w")
f.write("Hello\n")
f.write("a@text.com\n")
f.write("Call 9876543210\n")
f.write("Hello\n")
f.close()

f=open("day22_hidePii.txt","r")
lines=f.readlines()
f.close()
seen=[]

for line in lines:
    line=line.strip()
    h=make_hash(line)
    if h in seen:
        print(line,"---> Duplicate")
    else:
        seen.append(h)
        result=check_pii(line)
        hidden=hide_pii(line)
        print(line,"---> New ","-",result,"--Hidden:",hidden)
