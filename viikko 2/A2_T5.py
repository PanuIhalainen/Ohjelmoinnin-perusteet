def get_compound_word():
    while True:
        word = input("Insert a closed compound word: ").strip()
        if word:
            return word
        print("The word cannot be empty. Please try again.")

def parse_index(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            return None
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer or leave blank.")

def main():
    print("Program starting.\n")

    word = get_compound_word()
    reversed_word = word[::-1]
    length = len(word)
    last_char = word[-1]

    print(f"The word you inserted is '{word}' and in reverse it is '{reversed_word}'.")
    print(f"The inserted word length is {length}")
    print(f"Last character is '{last_char}'")

    print("\nTake substring from the inserted word by inserting...")


    start = parse_index("Starting point: ")
    end = parse_index("Ending point: ")
    step = parse_index("Step size: ")

    sliced = word[start:end] if step is None else word[start:end:step]
    print(f"\nThe word '{word}' sliced to the defined substring is '{sliced}'")

    print("\nProgram ending.")

if __name__ == "__main__":
    main()

