# Las tuplas son inmutables --- las tuplas manejan parentesis

frutas= ("Naranja","Platano","Guayaba")
print(frutas)

# saber largo
print(len(frutas))

# Acceder a valor mediante indice
print(frutas[0])

# Navegacion inversa
print(frutas[-1])

# Acceder a un rango de valores

print(frutas[0:1]) # Sin incluir el ultimo indice


#NOTA cuando es un solo dato en una tupla se tiene que poner la coma al final del primer elemento para indicar que ya no hay mas elementos

for frut in frutas:
    print(frut, end=" ")

#Para modificar una tupla primero tenemos que convertirla a una lista

frutaslist = list(frutas)

frutaslist[0] = "pera"

frutas=tuple(frutaslist)

print("\n",frutas)

#eliminar tupla
del frutas
print(frutas)
