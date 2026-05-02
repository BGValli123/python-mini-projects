import re

print("="*50)
print("🔐 Smart Password Strength Checker")
print("="*50)

def check_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")

    # Digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include numbers")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add special characters")

    return score, feedback

# 🔁 Loop
while True:
    password = input("\nEnter password (or type 'exit'): ")

    if password.lower() == "exit":
        print("👋 Exiting Password Checker")
        break

    score, feedback = check_password(password)

    print("\n🔍 Analysis:")

    if score <= 2:
        print("🔴 Weak Password")
    elif score == 3 or score == 4:
        print("🟡 Medium Password")
    else:
        print("🟢 Strong Password")

    print(f"Score: {score}/5")

    if feedback:
        print("\n💡 Suggestions:")
        for f in feedback:
            print(f)
    else:
        print("✅ Excellent password!")

    print("-"*50)
