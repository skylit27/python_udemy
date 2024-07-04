#Funcion sin parametros

def myFunction():
    print("Saludos desde mi funcion")

myFunction()

#Funcion con parametros

def myFunctionWithParameters(name, LastName):
    print(f"Mi nombre es: {name} y mi apellido es {LastName}")


myFunctionWithParameters("Oce","Skylit")

#Funcion 2 valores

def sum(a,b):
    return int(a) + int(b)

#uso de la funcion y asignacion a una variable
val = sum(5,6)

print(val)
print(sum(10,20))

# Valores por default

def sum2(a=1,b=222) -> int: #agregando pista de lo que va a retornar la funcion
    return a+b

print(sum2())
print(sum2(15,100))