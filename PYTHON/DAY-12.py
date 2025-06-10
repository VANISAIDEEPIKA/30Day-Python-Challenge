import re

def is_valid_email(email):
    # Pattern to match typical email formats
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

# List of sample emails to test
emails = ["test@example.com", "bad-email@", "hello@domain.co"]

for email in emails:
    result = "Valid" if is_valid_email(email) else "Invalid"
    print(f"{email} => {result}")