def fusionner_dicts(dict1, dict2):
    fusion = dict1.copy()
    for key, value in dict2.items():
        fusion[key] = fusion.get(key, 0) + value
    return fusion

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
resultat = fusionner_dicts(dict1, dict2)
print(resultat)  