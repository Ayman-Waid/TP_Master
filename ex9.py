def analyser_fichier(fichier_nom):
    try:
        with open(fichier_nom, 'r') as fichier:
            lignes = 0
            mots = 0
            caracteres = 0

            for ligne in fichier:
                lignes += 1
                mots += len(ligne.split())  
                caracteres += len(ligne) 

            print(f"Nombre total de lignes : {lignes}")
            print(f"Nombre total de mots : {mots}")
            print(f"Nombre total de caractères : {caracteres}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier_nom}' n'a pas été trouvé.")

file = "TP_N5/journal.txt"
analyser_fichier(file)
