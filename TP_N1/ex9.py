def analyse_texte(texte):
    mots = texte.split()
    return {
        "nombre_de_mots": len(mots),
        "nombre_de_caracteres": len(texte)
    }


texte = "Bonjour, comment allez-vous ?"
resultat = analyse_texte(texte)
print(resultat)
