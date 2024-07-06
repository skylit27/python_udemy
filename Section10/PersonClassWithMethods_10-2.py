class PersonaArgs:
    def __init__(self, name, lastname, age, *valores, **terminos):
        self.name = name
        self.lastname = lastname    #lado izquierdo atributos y lado derecho parametros
        self.age = age
        self.valores = valores
        self.terminos = terminos

    def showDetails(self): #se utiliza self para hacer referencia a la clase, cuando se crea un metodo en esta
        print(f"Objeto persona  = {self.name}, {self.lastname}, {self.age},{self.valores},{self.terminos}") # Se usa self para acceder al atributo de la clase



#NOTA: El operador self se conoce en otros lenguages de programacion como this, no es necesario que se llame self en python puede llamarse this

persona1 = PersonaArgs('Oce', 'Skylit', '25', "54654156554",2,3,4,5,m="manzana",p="pera")
persona1.showDetails()

#Modificando atributos

persona1.name = "Ocelote"
persona1.lastname = "DRackoss"
persona1.age = 26

persona1.showDetails()

persona2 = PersonaArgs('Cesar', 'Sanchez', '25')
persona2.showDetails()



#####################################################

#Otra manera de usar metodos de una clase es pasandole la referencia a una clase ejemplo

PersonaArgs.showDetails(persona1)

#Podemos agregar un atributo extra aunque no este en la clase pero este no es compartido con otras clases, NO ES COMUN

persona3 = PersonaArgs('Marco', 'Sanchez', '23')
persona3.job = "Programmer"

print(persona3.job)