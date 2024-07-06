def numberFactorial(number):
    if number == 1:
        return 1
    else:
        return number * numberFactorial(number-1)

numb= 5
value = numberFactorial(numb)
print(f"El factorial de {numb} es {value}")
