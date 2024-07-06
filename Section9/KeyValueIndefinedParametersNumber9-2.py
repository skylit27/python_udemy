def ListTerms(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value}')

ListTerms(IDE ="Integrated Development Enviroment", PK = "Primary Key")
