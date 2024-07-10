from Inheritance_12 import * #importamos todas las clases de archivo Inheritance


persona1 = person("Juan",25)
print(persona1) #Se sobreescribio el metodo en la clase Person ahora retorna el nombre y la edad

empleado1 = employee("Juan",25, 5000)
print(empleado1) # si no sobreescribimos el metodo en la clase hija agarra el de la clase padre (person) y este no tiene el atributo de sueldo por lo tanto no lo muestra

