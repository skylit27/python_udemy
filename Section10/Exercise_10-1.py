class cube:
    def __init__(self,width,deep,height):
        self.width = width
        self.deep = deep
        self.height = height


    def volume(self):
        return self.width*self.deep*self.height



width = int(input("Ingrese el ancho del cubo: "))
deep = int(input("Ingrese la profundidad del cubo: "))
height = int(input("Ingrese la altura del cubo: "))

cube = cube(width,deep,height)
result = cube.volume()

print(f"Volumen del cubo: {result}")