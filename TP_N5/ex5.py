import json

mon_fichier = "TP_N5/etudiants.json"

with open(mon_fichier, 'r') as file:
    data = json.load(file)

etudiants = data['etudiants']

for nom, infos in etudiants.items():
    print(f"Nom: {nom}")
    print(f"Âge: {infos['age']}")
    print(f"Note: {infos['note']}")
    print("-" * 40)
