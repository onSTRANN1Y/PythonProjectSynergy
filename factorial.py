import math as m

def is_factorial():
    try:
        num = int(input("Enter a number: "))

        if num < 0:
            return "Число не может быть отрицательным"

        return m.factorial(num)

    except ValueError:
        return "Нужно вводить целое число"

print(is_factorial())