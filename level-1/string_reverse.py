print("="*40)
print("🔤 String Reversal Program")
print("="*40)

# Input from user
user_input = input("Enter a string: ")

# 1. Using function (slicing)
def reverse_string(s):
    return s[::-1]

print("\n--- Using Function ---")
print("Reversed string:", reverse_string(user_input))


# 2. Using slicing directly
print("\n--- Using Slicing ---")
print("Reversed string:", user_input[::-1])


# 3. Using loop
loop_result = ""
for char in user_input:
    loop_result = char + loop_result

print("\n--- Using Loop ---")
print("Reversed string:", loop_result)


# 4. Using reversed() function
reversed_func_result = "".join(reversed(user_input))

print("\n--- Using reversed() ---")
print("Reversed string:", reversed_func_result)


# 5. Using while loop
while_result = ""
i = len(user_input) - 1

while i >= 0:
    while_result += user_input[i]
    i -= 1

print("\n--- Using While Loop ---")
print("Reversed string:", while_result)
