def celsius_to_fahrenheit(celsius):
    return round((celsius * 1.8) + 32, 1)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) / 1.8, 1)

def main():
    print("Program starting.\n")

    print("Options:")
    print("1--Celsius-to-Fahrenheit")
    print("2--Fahrenheit-to-Celsius")
    print("0--Exit")

    choice = input("Your choice: ").strip()

    if choice == "1":
        try:
            celsius = float(input("Insert the amount of Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius:.1f} °C equals to {fahrenheit:.1f} °F")
        except ValueError:
            print("Invalid temperature input.")
    elif choice == "2":
        try:
            fahrenheit = float(input("Insert the amount of Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.1f} °F equals to {celsius:.1f} °C")
        except ValueError:
            print("Invalid temperature input.")
    elif choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
    