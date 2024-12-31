from abc import ABC , abstractmethod


class forme(ABC):
    @abstractmethod
    def calcul_surface(self):
        pass

class cercle(forme) : 
    def __init__(self,rayon): 
        self.rayon = rayon

    def calcul_surface(self): 
        return 3.14 * self.rayon ** 2
    
class rectangle(forme) :
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def calcul_surface(self): 
        return self.largeur * self.hauteur
    
Cercle = cercle(5)
Rectangle  = rectangle(6,8)

print(Cercle.calcul_surface())
print(Rectangle.calcul_surface())