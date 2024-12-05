class CompteBancaire: 
    def __init__(self, titulaire, solde): 
        self.titulaire = titulaire
        self.solde = solde
    
    def deposer(self, montant): 
        self.solde += montant
    
    def retirer(self, montant):
        if montant <= self.solde: 
            self.solde -= montant
        else: 
            print("Impossible de retirer ce montant.")

    def afficher_solde(self):
        print(f"Le solde du compte de {self.titulaire} est de {self.solde} DH.")

MonCompte = CompteBancaire("Ayman", 2000)
MonCompte.deposer(500)
MonCompte.afficher_solde()
MonCompte.retirer(300)
MonCompte.afficher_solde()
MonCompte.retirer(7000)