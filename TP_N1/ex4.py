def compte_occurences(liste):
    counted = set()  
    for i in liste:
        if i not in counted:
            s = liste.count(i)  
            print(i, s)
            counted.add(i)  
test = ["ayman", "samir", "ayman", "morad"]
compte_occurences(test)
