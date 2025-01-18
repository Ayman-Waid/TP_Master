nom_fichier = "TP_N5/phrases.txt"

while True:
    reponse = input("Tu veux ajouter plus de phrases ? : ")

    if reponse.lower() == "oui":
        phrase = input("Entrez la phrase : ")

        with open(nom_fichier, "a"
        ) as fichier:
            fichier.write(phrase + "\n")
    else:
        print("Au revoir!")
        break
