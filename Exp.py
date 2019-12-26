print("This program do exponentiations.")
while True:
    base = int(input("Enter the base number: "))
    exp = int(input("Enter the exponent: "))
    result = 1
    for index in range(exp):
        result = result * base
    print(result)
    pass