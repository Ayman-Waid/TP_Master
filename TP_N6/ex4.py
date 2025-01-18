class NegativeAgeError(Exception) : 
    pass
def setAge(age):
    if age < 0 :
        raise NegativeAgeError("L'âge ne peut pas être négatif.")
   