def intersection(e1,e2):
    e3 = set()
    e3.update(e1,e2)
    return e3


a = {1,2,8,9,"ayman"}
b = {8,9,0,3,"test"}
print(intersection(a,b))


