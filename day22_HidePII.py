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