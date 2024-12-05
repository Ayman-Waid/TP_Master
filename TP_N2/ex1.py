class chien : 
    
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age
        
    def aboyer(self):
        print("Woof")

    def display(self):
        print(f"Mon chien est un {self.race} de nom {self.nom} et il a {self.age} ans")
    
Monchien = chien("chien","berger",2)

Monchien.aboyer()
Monchien.display()