import re
print("="*50)
print("🔁  Palindrome Checker")
print("="*50)
while True:
    text = input("\nEnter text (or type 'exit' to quit): ").strip()

    if text.lower() == "exit":
        print("👋 Exiting Palindrome Checker. Thank you!")
        break
    # 🔹 Clean input (remove spaces & special characters)
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()

    reversed_text = cleaned[::-1]

    print("\nProcessed Text :", cleaned)
    print("Reversed Text  :", reversed_text)

    if cleaned == reversed_text:
        print("✅ It is a Palindrome")
    else:
        print("❌ Not a Palindrome")

    print("-"*50)
