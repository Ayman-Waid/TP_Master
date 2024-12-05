class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"Voiture : {self.marque} {self.modele} ({self.annee})")

voiture1 = Voiture("dacia", "logan", 2020)
voiture2 = Voiture("Honda", "supra", 1998)
voiture3 = Voiture("Ford", "Mustang", 2021)

voiture1.afficher_info()
voiture2.afficher_info()
voiture3.afficher_info()
