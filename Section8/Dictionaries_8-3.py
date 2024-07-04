# Dictionaries KEY:VALUE


diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Objet Oriented Programming",
    "DBMS": "Database Management System"
}

print(diccionario)

# Largo

print(len(diccionario))

#Acceder a un elemento (key)

print(diccionario["IDE"])

#Otra forma de retornar un elemento
print(diccionario.get("OOP"))

# Modificando elementos
diccionario["OOP"] = "integrated development environment"

print(diccionario)

#Recorrer los elementos de un diccionario

#Buscar por llave y valor
for key, value in diccionario.items():
    print(key, value)

#Buscar por llave

for llave in diccionario.keys():
    print(llave)

#Buscar por valor

for valor in diccionario.values():
    print(valor)

#Validar existencia de un elemento

print("IDE" in diccionario)  #Retorna true si existe

#Agregar elemento a diccionario

diccionario["PK"] = "Primary key"

print(diccionario) #no es posible

#Remover elemento

diccionario.pop("DBMS")
print(diccionario)

#limpiar diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario
print(diccionario)
