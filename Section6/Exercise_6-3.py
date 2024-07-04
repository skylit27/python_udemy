calification = float(input("Proporciona un valor entre 0 y 10"))
message = None

if calification >= 9 and calification <= 10:
    message = "A"
elif calification >= 8 and calification < 9:
    message = "B"
elif calification >= 7 and calification < 8:
    message = "C"
elif calification >= 6 and calification < 7:
    message = "D"
elif calification >= 0 and calification < 6:
    message = "F"
else:
    message = "Valor incorrecto"

print(message)

