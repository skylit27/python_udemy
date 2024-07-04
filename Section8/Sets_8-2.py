# Los sets no tienen un orden y no permite modificar los elementos pero si agregar y eliminar, y no permite duplicados

#set

planetas = {"Marte","Jupiter","Venus"}
print(planetas)

#largo
print(len(planetas))

#Revisar si un elemento esta presente

print("Marte" in planetas) #Retorna True

#Agregar un elemento

planetas.add("Tierra")

print(planetas)

#No soporta elementos duplicados

planetas.add("Tierra")
print(planetas)

#Eliminar Elemento posiblemente arrojando un error

planetas.remove("Tierra")
print(planetas)

#Eliminar Elemento sin arrojar error en caso de que no se encuentre

planetas.discard("Venus")
print(planetas)

# limpiar por completo
planetas.clear()

# eliminar set

del planetas