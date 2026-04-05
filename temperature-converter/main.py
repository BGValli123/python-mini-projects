print("="*45)
print("   🌡️ Advanced Temperature Converter")
print("="*45)

history=[]

while True:
    print("\nChoose conversion:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. View History")
    print("6. Exit")
    print("7. Clear History")

    choice = input("Enter choice (1-6): ").strip()

    if choice == "6":
        print("👋 Exiting program. Thank you!")
        break

    elif choice == "5":
        print("\n📜 Conversion History:")
        if not history:
            print("No conversions yet.")
        else:
            for item in history:
                print(item)
        continue

    if choice not in ["1", "2", "3", "4"]:
        print("❌ Invalid choice! Please select 1–6.")
        continue

    try:
        temp = float(input("Enter temperature: "))
    except ValueError:
        print("❌ Invalid input! Please enter a numeric value.")
        continue

    # Absolute zero check
    if temp < -273.15:
        print("❌ Temperature below absolute zero!")
        continue

    if choice == "1":
        result = (temp * 9/5) + 32
        output = f"{temp}°C → {round(result,2)}°F"

    elif choice == "2":
        result = (temp - 32) * 5/9
        output = f"{temp}°F → {round(result,2)}°C"

    elif choice == "3":
        result = temp + 273.15
        output = f"{temp}°C → {round(result,2)}K"

    elif choice == "4":
        result = temp - 273.15
        output = f"{temp}K → {round(result,2)}°C"

    print("\n" + "="*40)
    print("✅ Result:", output)
    print("="*40)

# Save to history
    history.append(output)
