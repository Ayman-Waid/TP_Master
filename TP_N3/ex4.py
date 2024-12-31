class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    def calculer_prix_avec_remise(self, remise, montant_minimum):
        if self.__prix > montant_minimum:
            return self.__prix * (1 - remise)
        return self.__prix
