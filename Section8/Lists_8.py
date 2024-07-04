nombre = ["Juan","Karla","Ricardo","Maria"]

# Imprimir la lista de nombre
print(nombre)

#Acceder a valor en especifico
print(nombre[3])

#Acceder a los elementos de manera inversa
print(nombre[-1])

#Acceder a un rago de valores en la lista

print(nombre[0:2]) #Solo retorna los elementos 0 y 1

#Ir del inicio al indice sin incluirlo

print(nombre[:3])

#Ir desde el indice indicado hasta el final

print(nombre[0:])

# Cambiar un valor de la lista

nombre[2] = "Skylit"
print(nombre)


#recorrer la lista completa
for nom in nombre:
    print(nom)
else:
    print("No existen los nombres en la lista")

#Numero de elementos en nuestra lista

print(len(nombre))

# agregar un elemento al final de la lista

nombre.append("Oce")
print(nombre)

# agregar un elemento en una posicion especifica

nombre.insert(0,32) #Recorre el elemento que esta en esa posicion a la derecha
print(nombre)

# Remover elemento

nombre.remove(32) #valor del elemento "NO" posicion
print(nombre)

#Remover el ultimo valor agregado a nuestra lista (usamos pop)

nombre.pop()
print(nombre)

# Eliminar elemento mediante un indice (usamos del)

del nombre[2]

print(nombre)

#limpiar lista
nombre.clear()
print(nombre)