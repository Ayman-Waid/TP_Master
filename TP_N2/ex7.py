class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            print(f"Titre: {livre.titre}, Auteur: {livre.auteur}, Annee: {livre.annee_publication}")

livre1 = Livre("La boite a merveille", "ahmed safrioui", 1949)
livre2 = Livre("derniere jour d un condamne", "vector hugo", 1829)

bibliotheque = Bibliotheque()
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)

bibliotheque.afficher_livres()
