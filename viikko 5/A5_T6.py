print("Program starting.")
def showOptions():
    print("Options:")
    print("1--Show-count")
    print("2--Increase-count")
    print("3--Reset-count")
    print("0--Exit")

def askChoice():
    choice = input("Your-choice:")
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown-option!")
        return -1  # Palautetaan virheellinen valinta

def main():
    print("Program-starting.")
    count = 0

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current-count--{count}")
        elif choice == 2:
            count += 1
            print("Count-increased!")
        elif choice == 3:
            count = 0
            print("Count-reset!")
        elif choice == 0:
            print("Exiting-program.")
            break
        elif choice == -1:
            pass  # Unknown-option jo tulostettu
        else:
            print("Unknown-option!")

    print("Program-ending.")
    