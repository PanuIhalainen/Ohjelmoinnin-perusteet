def multiply_digits(n):
    result = 1
    digits = [int(d) for d in str(n)]
    for d in digits:
        result *= d
    return result, digits

# Pääohjelma
print("Program: starting.")
print("\nCheck multiplicative persistence.")
num = int(input("Insert an integer: "))

steps = 0

while num >= 10:
    product, digits = multiply_digits(num)
    print(".*.".join(str(d) for d in digits), "=", product)
    num = product
    steps += 1

print(f"\nThis program took {steps} step(s)")
print("Program: ending.")
