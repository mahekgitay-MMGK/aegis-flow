"""Theory: using regular expressions to recognize PII.

Personally identifiable information (PII) is information that can identify a
person, either by itself (for example, an email address) or when combined with
other information. Common examples include email addresses, phone numbers,
government identifiers, and payment-card numbers.

Regular expressions (regex) describe text patterns. They are useful for
finding likely PII in unstructured text, but a match is only a candidate: a
regex cannot establish who a value belongs to or whether it is genuine.

Basic regex building blocks
---------------------------
	[0-9]       one digit
	[A-Za-z]    one ASCII letter
	\d          a digit (Unicode-aware in Python by default)
	{n,m}       repeat the preceding expression n through m times
	?           make the preceding item optional
	|           alternative (OR)
	(...)       group expressions
	\b          boundary between a word and non-word character
	^ and $     beginning and end of a string (with flags, line semantics vary)

For example, ``r"\\b\\d{3}-\\d{2}-\\d{4}\\b"`` describes a US-style
identifier with three digits, a hyphen, two digits, another hyphen, and four
digits. It checks the shape only; it does not validate issuance or ownership.
Similarly, a basic email pattern can locate strings containing a local part,
``@``, and a domain, but complete email validation requires more than a simple
regex and often should be delegated to a trusted library or confirmation flow.

Designing PII patterns
----------------------
1. Define the format and the text context in which it may appear.
2. Allow realistic separators and formatting variations where appropriate.
3. Use boundaries or surrounding context to reduce partial matches.
4. Add format-specific validation when needed (for example, a checksum), while
   remembering that validation still does not prove identity.
5. Test both expected matches and near-misses, including punctuation, spaces,
   Unicode, and overlapping values.

Limitations and safe handling
-----------------------------
Regex-based detection can produce false positives and false negatives. Formats
vary by country, and the same digit sequence may be ordinary text in one
context and sensitive in another. Treat matches as signals for review, not as
proof. Avoid logging matched values; mask or redact them, restrict access to
the source text, and retain only what the application needs. Prefer established
data-loss-prevention or validation tools for production systems.
"""
