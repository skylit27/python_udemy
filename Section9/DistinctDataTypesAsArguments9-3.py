def deployNames(names):
    for nombre in names:
        print(nombre)

names =["Oce","Skylit","DRackoss227"]
deployNames(names)

deployNames("Skylit") #Lo imprime por letra ya que es una lista de caracteres

deployNames((10,11)) #los itera por que es una tupla si estuvieran solos los toma como int
deployNames([10,20])