"""Theory of personally identifiable information (PII) detection.

PII is information that can identify a person directly or when combined with
other data. Direct identifiers include names, email addresses, phone numbers,
government ID numbers, and account numbers. Quasi-identifiers, such as a date
of birth or location, may identify someone in combination.

Detection methods commonly include:
* Pattern matching: regular expressions find structured values such as emails,
	phone numbers, and ID formats. Validation and context checks reduce false
	positives.
* Named-entity recognition: language models identify contextual entities such
	as people's names, organizations, and locations in unstructured text.
* Dictionaries and rules: domain-specific terms and surrounding words help
	recognize identifiers that lack a reliable fixed format.

A practical detector combines these methods, records the type and location of
each match, and evaluates precision (the fraction of flagged values that are
PII) and recall (the fraction of actual PII that is found). False positives
and false negatives are both important: excessive redaction harms usefulness,
while missed PII can expose people.

Detection is context-dependent and cannot guarantee that data is anonymous.
Review findings, minimize collected data, apply appropriate masking or
redaction, and protect any retained results. Requirements and definitions of
PII vary by jurisdiction and use case, so detection should support—not replace—
privacy and legal review.
"""

# Example
text="my email is mahek@gmail.com and phone is 9876554321"

if "@" in text:
    print(" PII found - Email _ stop or Hide")
else:
    print("NO pII - Safe -send")

if "9876554321" in text:
    print("PII found - Email _ stop or Hide")
else:
    print("NO pII - Safe -send")