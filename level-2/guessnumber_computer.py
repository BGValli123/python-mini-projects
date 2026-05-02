print("="*50)
print("🤖 Smart Computer Number Guesser")
print("="*50)

def play_game():
    print("\nChoose Difficulty:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–500)")

    choice = input("Enter choice: ")

    if choice == "1":
        low, high = 1, 50
    elif choice == "2":
        low, high = 1, 100
    elif choice == "3":
        low, high = 1, 500
    else:
        print("❌ Invalid choice. Defaulting to Medium.")
        low, high = 1, 100

    print(f"\nThink of a number between {low} and {high}")
    input("Press Enter when ready...")

    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"\n🤖 My guess is: {guess}")

        feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()

        if feedback == "c":
            print(f"\n🎉 I guessed your number in {attempts} attempts!")
            return

        elif feedback == "h":
            high = guess - 1

        elif feedback == "l":
            low = guess + 1

        else:
            print("❌ Invalid input! Please enter h, l, or c.")
            attempts -= 1  # don't count invalid input
            continue

    # If logic breaks
    print("\n⚠️ Inconsistent hints detected!")
    print("Please restart and give correct responses.")

# 🔁 Game loop
while True:
    play_game()

    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing!")
        break
