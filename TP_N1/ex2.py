def max_tuple(test):
    max_value = test[0]
    for i in test:
        if i > max_value:
            max_value = i
    return max_value

data_tuple = (1, 2, 3, 4, 5)
print(max_tuple(data_tuple))

