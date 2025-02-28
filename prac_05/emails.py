"""
Word Occurrences
Estimate: 12 minutes
Actual:   10 minutes
"""


def extract_name_from_email(email):
    """Extracts the name from the email by splitting the email and converting it to title case."""
    name_part = email.split('@')[0]
    name = name_part.replace('.', ' ').title()
    return name


def main():
    email_to_name = {}
    while True:
        email = input("Email: ").strip()
        if not email:
            break
        name = extract_name_from_email(email)
        is_correct = input(f"Is your name {name}? (Y/n): ").strip().lower()
        if is_correct not in ('y', ''):
            name = input("Name: ").strip()
        email_to_name[email] = name

    # Print all emails and names
    for email, name in email_to_name.items():
        print(f"{name} ({email})")



if __name__ == "__main__":
    main()