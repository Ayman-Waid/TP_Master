class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

mon_rectangle = Rectangle(5, 10)

print(f"Surface du rectangle : {mon_rectangle.calculer_surface()}")
print(f"Perimetre du rectangle : {mon_rectangle.calculer_perimetre()}")
