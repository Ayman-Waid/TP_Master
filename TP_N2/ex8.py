class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.amis = []

    def ajouter_ami(self, ami):
        self.amis.append(ami)

    def afficher_amis(self):
        if self.amis:
            print(f"Liste des amis de {self.prenom} {self.nom} :")
            for ami in self.amis:
                print(f"{ami.prenom} {ami.nom}")
        else:
            print(f"{self.prenom} {self.nom} n'a pas d'amis.")

personne1 = Personne("ayman", "waid", 30)
personne2 = Personne("yahya", "bouarfa", 25)
personne3 = Personne("ali", "omari", 28)

personne1.ajouter_ami(personne2)
personne1.ajouter_ami(personne3)

personne1.afficher_amis()
