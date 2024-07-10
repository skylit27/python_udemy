class person: #todas las clases heredan de la clase Object
        def __init__(self, name, age):
            self.name = name
            self.age = age                  #Queda pendiente encapsular todo este archivo

        def __str__(self): #Estamos sobreescriendo el metodo __str__ de la clase padre (Object) ya que es el padre de todas las clases
            return f"Persona {self.name} - {self.age}" #este metodo se manda a llamar de manera automatica (cuando imprimimos la instancia del objeto) ver ClientPerson
class employee(person): #heredamos de la clase person
    def __init__(self, name, age, salary): #agregamos los los mismos parametros que tiene la clase padre
        super().__init__(name, age) #mandamos a llamar el metodo de la clase padre con super() y le mandamos los parametros
        self.salary = salary

    def __str__(self):
        return super().__str__() + f"- salary: {self.salary}" #Reutilizamos el metodo de la clase padre pero le agregamos el atributo sueldo


# empleado = employee('Juan', 25, 5000)
# print(empleado.name)
# print(empleado.age)
# print(empleado.salary)