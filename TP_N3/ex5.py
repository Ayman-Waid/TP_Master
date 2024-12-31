class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes = []

    def ajouter_employe(self, employe):
        self.employes.append(employe)

    def afficher_employes(self):
        for employe in self.employes:
            print(f"{employe.nom} {employe.prenom}")
