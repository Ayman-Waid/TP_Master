def carre(x):
    return (lambda n: n**2)(x)

nombre = 5
print(f"Le carre de {nombre} est {carre(nombre)}")
