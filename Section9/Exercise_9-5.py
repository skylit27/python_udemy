def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def converter():
    selection = int(input("""
    Ingresa el numero segun el tipo de conversion que quieres hacer:
    1.- Celsius a Fahrenheit
    2.- Fahrenheit a Celsius
    
    Seleccion: 
    """))

    if(selection == 1):
        cels = int(input("Ingresa los grados Celsius"))
        print(f"El resultado de los grados Fahrenheit es: {celsiusToFahrenheit(cels)}")
    elif(selection == 2):
        fahren = int(input("Ingresa los grados Fahrenheit"))
        print(f"El resultado de los grados Celsius es: {celsiusToFahrenheit(fahren)}")
    else:
        print("El valor ingresado esta fuera de rango")

converter()

