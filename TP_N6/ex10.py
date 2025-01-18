def read_file_content():
    while True:
        try:
            file_name = input("Veuillez saisir le nom du fichier à lire : ")
            with open(file_name, 'r') as file:
                content = file.read()
                print("\nContenu du fichier :\n")
                print(content)
                return content
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{file_name}' n'a pas été trouvé. Essayez encore.")
        except PermissionError:
            print(f"Erreur : Vous n'avez pas les permissions nécessaires pour lire '{file_name}'.")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

def get_positive_integer():
    while True:
        try:
            user_input = input("Veuillez saisir un entier positif : ")
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Erreur : Le nombre doit être un entier strictement positif. Essayez encore.")
        except ValueError:
            print("Erreur : Entrée invalide. Veuillez saisir un entier valide.")

def main():
    print("Bienvenue dans le programme de lecture de fichier et de saisie d'entier.")
    file_content = read_file_content()
    print("\nFichier lu avec succès.")
    positive_integer = get_positive_integer()
    print(f"\nVous avez saisi l'entier positif : {positive_integer}")

if __name__ == "__main__":
    main()
