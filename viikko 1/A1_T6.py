
Feed = input("Insert an integer: ")         # Pyydetään käyttäjää syöttämään kokonaisluku
Value = int(Feed)                       # Muutetaan syöte kokonaisluvuksi
Remainder = Value % 2                   # Lasketaan jakojäännös jakamalla kahdella
print(f"Value is {Value}")          # Tulostetaan syötetty arvo
print(f"The remainder is {Remainder} when {Value} is divided by 2.")        # Tulostetaan jakojäännös
