class PersonaArgs:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname    #lado izquierdo atributos y lado derecho parametros
        self.age = age

persona1 = PersonaArgs('Oce', 'Skylit', '25')
print(f"Objeto persona 1 = {persona1.name}, {persona1.lastname}, {persona1.age}")

#Modificando atributos

persona1.name = "Ocelote"
persona1.lastname = "DRackoss"
persona1.age = 26


persona2 = PersonaArgs('Cesar', 'Sanchez', '25')
print(f"Objeto persona 2 = {persona2.name}, {persona2.lastname}, {persona2.age}")