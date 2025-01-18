phrases = []
for i in range(1, 4):
    phrase = input(f"Entrez la phrase {i} : ")
    phrases.append(phrase)

nom_fichier = "TP_N5/phrases.txt"

with open(nom_fichier, "w") as fichier:
    for phrase in phrases:
        fichier.write(phrase + "\n")

