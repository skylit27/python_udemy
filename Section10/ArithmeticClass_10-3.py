class ArithmeticClass:
    """
    Clase aritmetica para realizar las operaciones de sumar, restar, etc
    """
    def __init__(self, operatorA, operatorB):
        self.operatorA = operatorA
        self.operatorB = operatorB

    def sigma(self):
        return self.operatorA + self.operatorB

    def substract(self):
        return self.operatorA - self.operatorB

    def division(self):
        return self.operatorA / self.operatorB


aritmetica1 = ArithmeticClass(10,5 )
print(aritmetica1.sigma())
print(aritmetica1.substract())
print(aritmetica1.division())