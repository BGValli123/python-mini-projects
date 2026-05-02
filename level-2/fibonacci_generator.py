print("="*50)
print("📈 Fibonacci Sequence Generator")
print("="*50)

def generate_fibonacci(n):
    sequence = []

    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

# 🔁 Loop
while True:
    user_input = input("\nEnter number of terms (or 'exit'): ")

    if user_input.lower() == "exit":
        print("👋 Exiting Fibonacci Generator")
        break

    if not user_input.isdigit():
        print("❌ Please enter a valid positive number!")
        continue

    n = int(user_input)

    if n <= 0:
        print("❌ Number must be greater than 0")
        continue

    fib_sequence = generate_fibonacci(n)

    print("\n📊 Fibonacci Sequence:")
    print(fib_sequence)

    print("-"*50)
