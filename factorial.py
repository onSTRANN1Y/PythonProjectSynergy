import math as m

try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Число не может быть отрицательным")
    else:
        result = m.factorial(num)
        print(result)
except ValueError:
    print("Нужно вводить целое число")