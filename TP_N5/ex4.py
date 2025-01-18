import csv

mon_fichier = "TP_N5/contacts.csv"

with open(mon_fichier, mode='r', newline='') as file:
    reader = csv.DictReader(file, delimiter=';')        
    for row in reader:
        print(f"Nom : {row['nom']}, Age : {row['age']}, Ville : {row['ville']}")