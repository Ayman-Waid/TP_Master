def process_input(user_input) : 
    try :
        number = int(user_input)
        result = number / 10
        print(f"result = {result}")
    except ValueError:
        print("Erreur : vous devez saisir un nombre entier.")
    except ZeroDivisionError:
        print("Erreur : vous ne pouvez pas diviser par zéro.")