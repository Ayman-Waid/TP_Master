def get_positive_integer():
    while True:
        try:
            user_input = input("Veuillez saisir un entier positif : ")
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Le nombre doit être un entier positif. Essayez encore.")
        except ValueError:
            print(  "Entrée invalide. Veuillez saisir un entier valide.")
