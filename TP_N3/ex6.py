class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def calculer_total(self):
        return self.produit.calculer_prix_avec_remise(0, 0) * self.quantite

class Panier:
    def __init__(self):
        self.commandes = []

    def ajouter_commande(self, commande):
        self.commandes.append(commande)

    def calculer_total(self):
        return sum(commande.calculer_total() for commande in self.commandes)
