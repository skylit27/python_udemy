from Encapsulation_11 import Person
# from (nombre del archivo) import (nombre de la clase, si son todas ponemos *)


print("Creacion de objetos".center(50,"-"))
persona1 = Person("Karla","Gomez",33)
persona1.showDetails()
#print(__name__) #retorna main por que este es el modulo principal


print("Eliminacion de objetos".center(50,"-"))
del persona1 #se destruye el objeto y se llama al metodo __del__ de la clase Person