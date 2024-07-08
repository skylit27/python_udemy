class Person:
    def __init__(self, name, lastname, age, ):
        self._name = name
        #self.__name = name           # Para evitar el que el atributo no pueda ser modificado de manera estricta podemos usar "__"
        self._lastname = lastname
        self._age = age              #le ponemos "_" a los atributos self para indicar que no debemos acceder de manera directa al atributo
        # self._value = value
        # self._terms = terms       #se borran de los patametros del init el value y terms por cuestiones practicas

    @property #Este decorador nos permite acceder al metodo como si fuera un atributo en vez de un metodo
    def name(self): #metodo para obtener el nombre (get)
       # print("Llamamos al metodo get")
        return self._name

    @name.setter #Creamos el setter, al igual que el getter no necesitamos usarlo como metodo simplemente como atributo
    def name(self, name):
       # print("Llamamos al metodo set")
        self._name = name

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


    def showDetails(self):
        print(f"Persona: {self._name} {self._lastname} {self._age}")

    def __del__(self):
        print(f"Persona: {self._name} {self._lastname} {self._age}")


# El _ se utiliza solo para indicar que no debe de usarse el atributo sin embargo sin embargo si podemos acceder al atributo


if __name__ == "__main__":   #validacion de si el codigo se ejecuta desde la misma clase se ejecutara lo siguiente
    person1 = Person("Juan","Perez",28)
    #person1._name = "Juan Carlos"
    print(person1.name)
    person1.name = "Juan Carlos"
    print(person1.name)
    person1.lastname = "Lara"
    person1.age = 40
    person1.showDetails()


#NOTA: Cuando un metodo solo tiene el getter, es conocido como un atributo de solo lectura

print(__name__) #nos indica desde donde se esta ejecutando el codigo (si es desde la misma clase indicara main)