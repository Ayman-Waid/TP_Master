from abc import ABC, abstractmethod

class animal(ABC) : 
    @abstractmethod
    def faire_du_bruit(self) : 
        pass

class chat(animal) :
    def faire_du_bruit(self) :
        return "Miaou"
    
class chien(animal) :
    def faire_du_bruit(self) :
        return "Woof"
    
MonChien = chien()
Monchat = chat()
print(Monchat.faire_du_bruit())
print(MonChien.faire_du_bruit())
    