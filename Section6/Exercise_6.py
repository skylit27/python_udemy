numero = int(input("Proporciona un valor entre 1 y 3: "))
numeroTexto = ""


if numero == 1:
    numeroTexto = "Numero 1"
elif numero == 2:
    numeroTexto = "Numero 2"
elif numero == 3:
    numeroTexto = "Numero 3"
else:
    numeroTexto = "Valor fuera de rango"

print(f"Numero proporcionado: {numero}: {numeroTexto}")