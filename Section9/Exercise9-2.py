def descendent(number):
    if number >=1:
        print(number)
        descendent(number-1)
    elif number==0:
        return #no retornamos nada
    elif number<0:
        print("Valor incorrecto")

descendent(5)