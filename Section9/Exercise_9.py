def sumNumbers(*numbers): # Con pass podemos definir despues nuestra funcion
    resultado = 0
    for number in numbers:
        resultado += number
    return resultado



print(sumNumbers(1,2,3,4,5))