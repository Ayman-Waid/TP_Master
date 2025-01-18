nom_fichier = r"C:\Users\pc\Desktop\TP_Master\TP_N5\exemple.txt"

with open(nom_fichier, "r") as fichier:
    for numero, ligne in enumerate(fichier, start=1):
        print(f"Ligne {numero}: {ligne.strip()}")
