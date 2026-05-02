import math
print("="*50)
print("🔬 Scientific Calculator (Final Version)")
print("="*50)
print("💡 Use * for multiply, ** for power (e.g., 3*pi, e**2)")
print("💡 Angles are in degrees")
history = []
# 🔹 Expression mode
def evaluate_expression(expr):
    try:
        allowed = {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "pow": math.pow
        }
        result = eval(expr, {"__builtins__": None}, allowed)
        return round(result, 4)
    except Exception:
        return "❌ Invalid expression"
# 🔹 Arithmetic
def arithmetic():
    print("\nArithmetic Operations:")
    print("1. +  2. -  3. *  4. /  5. %  6. **  7. //")
    ch = input("Choose operation: ")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if ch == "1":
            return f"{a}+{b} = {round(a+b,4)}"
        elif ch == "2":
            return f"{a}-{b} = {round(a-b,4)}"
        elif ch == "3":
            return f"{a}*{b} = {round(a*b,4)}"
        elif ch == "4":
            if b == 0:
                return "❌ Division by zero"
            return f"{a}/{b} = {round(a/b,4)}"
        elif ch == "5":
            return f"{a}%{b} = {round(a%b,4)}"
        elif ch == "6":
            return f"{a}**{b} = {round(a**b,4)}"
        elif ch == "7":
            if b == 0:
                return "❌ Division by zero"
            return f"{a}//{b} = {a//b}"
        else:
            return "❌ Invalid choice"
    except ValueError:
        return "❌ Invalid input"
# 🔹 Trigonometry
def trigonometry():
    print("\nTrigonometric Functions:")
    print("1. sin  2. cos  3. tan  4. cosec  5. sec  6. cot")

    ch = input("Choose function: ")

    try:
        angle = float(input("Enter angle (degrees): "))
        if ch == "1":
            return f"sin({angle}) = {round(math.sin(math.radians(angle)),4)}"
        elif ch == "2":
            return f"cos({angle}) = {round(math.cos(math.radians(angle)),4)}"
        elif ch == "3":
            return f"tan({angle}) = {round(math.tan(math.radians(angle)),4)}"
        elif ch == "4":
            s = math.sin(math.radians(angle))
            if s == 0:
                return "❌ cosec undefined"
            return f"cosec({angle}) = {round(1/s,4)}"
        elif ch == "5":
            c = math.cos(math.radians(angle))
            if c == 0:
                return "❌ sec undefined"
            return f"sec({angle}) = {round(1/c,4)}"
        elif ch == "6":
            t = math.tan(math.radians(angle))
            if t == 0:
                return "❌ cot undefined"
            return f"cot({angle}) = {round(1/t,4)}"
        else:
            return "❌ Invalid choice"
    except ValueError:
        return "❌ Invalid input"
# 🔹 Logarithmic
def logarithmic():
    print("\nLog Functions:")
    print("1. log10  2. ln  3. sqrt")
    ch = input("Choose function: ")
    try:
        x = float(input("Enter number: "))
        if ch == "1":
            if x <= 0:
                return "❌ log undefined for non-positive values"
            return f"log({x}) = {round(math.log10(x),4)}"
        elif ch == "2":
            if x <= 0:
                return "❌ ln undefined for non-positive values"
            return f"ln({x}) = {round(math.log(x),4)}"
        elif ch == "3":
            if x < 0:
                return "❌ Cannot take sqrt of negative"
            return f"√{x} = {round(math.sqrt(x),4)}"
        else:
            return "❌ Invalid choice"
    except ValueError:
        return "❌ Invalid input"
# 🔹 Constants
def constants():
    print("\nConstants:")
    print("1. π  2. e")
    ch = input("Choose: ")
    if ch == "1":
        return f"π = {round(math.pi,4)}"
    elif ch == "2":
        return f"e = {round(math.e,4)}"
    else:
        return "❌ Invalid choice"
# 🔹 MAIN LOOP
while True:
    print("\nMain Menu:")
    print("1. Arithmetic")
    print("2. Trigonometry")
    print("3. Logarithmic")
    print("4. Constants")
    print("5. Expression Mode")
    print("6. View History")
    print("7. Clear History")
    print("8. Exit")
    choice = input("Enter choice: ")
    if choice == "8":
        print("👋 Exiting Calculator. Thank you!")
        break
    elif choice == "6":
        print("\n📜 History:")
        if not history:
            print("No history yet.")
        else:
            for h in history:
                print(h)
        continue
    elif choice == "7":
        history.clear()
        print("🗑️ History cleared!")
        continue
    elif choice == "5":
        print("💡 Example: 3*pi, sin(30), e**2")
        expr = input("Enter expression: ")
        result = evaluate_expression(expr)
        history.append(f"{expr} = {result}")
    elif choice == "1":
        result = arithmetic()
        history.append(result)
    elif choice == "2":
        result = trigonometry()
        history.append(result)
    elif choice == "3":
        result = logarithmic()
        history.append(result)
    elif choice == "4":
        result = constants()
        history.append(result)
    else:
        result = "❌ Invalid choice"
    print("\n" + "="*40)
    print("Result:", result)
    print("="*40)
