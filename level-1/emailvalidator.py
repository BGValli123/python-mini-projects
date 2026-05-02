import re

print("="*50)
print("📧 Smart Email Validator")

print("="*50)

common_domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def suggest_email(email):
    if "@" in email:
        parts = email.split("@")

        if len(parts) != 2:
            return None

        username, domain = parts

        if domain and "." not in domain:
            for d in common_domains:
                if domain.lower() in d:
                    return f"{username}@{d}"

    return None

def extract_details(email):
    username, domain = email.split("@")
    return username, domain

while True:
    email = input("\nEnter email (or type 'exit' to quit): ").strip()

    if email.lower() == "exit":
       print("👋 Exiting Email Validator. Thank you for using the system!")
       break

    if validate_email(email):
        username, domain = extract_details(email)

        print("\n✅ Valid Email Address")
        print(f"👤 Username : {username}")
        print(f"🌐 Domain   : {domain}")

        if domain in common_domains:
            print("⭐ Recognized popular domain")

    else:
        print("\n❌ Invalid Email Address")

        suggestion = suggest_email(email)

        if suggestion:
            print(f"💡 Did you mean: {suggestion}?")
            choice = input("👉 Type 'yes' to accept or 'no' to ignore: ").strip().lower()

            if choice == "yes":
                email = suggestion
                print("\n✅ Using suggested email...")

                username, domain = extract_details(email)
                print(f"👤 Username : {username}")
                print(f"🌐 Domain   : {domain}")

                if domain in common_domains:
                    print("⭐ Recognized popular domain")
            else:
                continue

        # Error messages
        if " " in email:
            print("⚠️ Email should not contain spaces")

        if "@" not in email:
            print("⚠️ Missing '@' symbol")

        elif email.count("@") != 1:
            print("⚠️ Email must contain exactly one '@'")

        else:
            username, domain = email.split("@")

            if username == "":
                print("⚠️ Username is missing before '@'")

            if domain == "":
                print("⚠️ Domain is missing after '@'")

            elif "." not in domain:
                print("⚠️ Domain must contain '.' (e.g., gmail.com)")
