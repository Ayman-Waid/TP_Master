try:
    with open('inexistant.txt', 'r') as fichier:
        contenu = fichier.read()
        print(contenu)
except FileNotFoundError:
    print("Erreur : Le fichier 'inexistant.txt' n'a pas été trouvé.")
