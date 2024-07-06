def numberMultiplier(*args):
    result = 1  #la tenemos que inicializar con  1 si no da error
    for num in args:
        result *= num
    return result


print(numberMultiplier(1,2,3,4,5))

