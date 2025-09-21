print("Hello World!")
print("Here we are")
print("He said: \"Hello\", and kept walking")
print("He said hello \n \r \t \b and \\ 'kept walking")

exampleString = "Text and numb3rs"      #tekstiä ja numeroita
exampleInt = 12                         #tasanumeroita
exampleFloat = 12.12                    #numeroita desimaalilla
exampleBoolean = False                  # True tai false

Firstname = input("What is your firstname: ")           # tallentaa muistiin tuon firstname
Lastname = input("What is your lastname: ")
print("Hello ", Firstname, Lastname)                    # pystyy käyttämään muistista

Sentence = "Finding substring"  
print(Sentence)                 
print(Sentence[0])              # Antaa lauseen ensimmäisen merkin
print(Sentence[-2])             # antaa lauseeen ja -2 taakse päin merkin
print(Sentence[2:9])            # Antaa lauseen merkit välistä 2-8
print(Sentence[:9])             # antaa merkit 9 asti
print(Sentence[-9:-2])          # antaa merkit lauseen ekasta lasketna -9--2
print(Sentence[2:9:3])          # askeleiden merkit, monta hypitään
print(Sentence[::3])
print(Sentence[::-1])

name = "Mira"
age = 48

print(name + " " + str(age))

num1 = input("Anna luku 1 ")
num2 = input("Anna luku 2 ")

num3 = int(num1) + int(num2)
print(num3)

