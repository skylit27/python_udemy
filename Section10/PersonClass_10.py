class Persona:
    def __init__(self):  # Metodo dunder (Double underscore, Este es inicializador, ya que en python no hay un contructor como tal
        self.name = "Juan"
        self.lastname = "Perez"  #no es comun agregar atributos de esta manera, adelante se vera como hacerlo con __init__
        self.age = 28



persona1 = Persona() #Aqui mandamos a llamar al metodo init

print(persona1.name)
print(persona1.lastname)
print(persona1.age)