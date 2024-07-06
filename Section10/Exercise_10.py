class rectangle:
    def __init__(self, width, height):
        
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


width = int(input("Ingrese la base: "))
height = int(input("Ingrese la altura: "))
result = rectangle(width,height)
print(result.area())