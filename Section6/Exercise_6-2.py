user = int(input("Proporciona tu edad: "))
mensaje =  None

if user >=0 and user <=10:
    mensaje= "La infancia es increible"
elif user > 10 and user <=20:
    mensaje= "Muchos cambios y mucho estudio"
elif user >20 and user <=30:
    mensaje ="Amor y comienza el trabajo"
else:
    mensaje ="Etapa de vida no reconocida"

print(f"Tu edad es {user}, {mensaje}")