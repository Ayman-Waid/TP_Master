def factorielle(n):
    if n == 0:  
        return 1
    elif n > 0:  
        return n * factorielle(n - 1)
    else:
        raise ValueError("La factorielle n'est pas définie pour les nombres négatifs.")


print(factorielle(5))