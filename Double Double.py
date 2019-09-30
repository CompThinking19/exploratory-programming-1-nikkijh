def triple(sequence):
    result = []
    for element in sequence:
        result = result + [element * 3]
    return result
#runs triple on the list
print triple([2, 4, 6, 8, 10])
#passes in list x to triple
x = [2, 4, 6, 8, 12]
print triple(x)
#triples the list and saves it as a variable
y = triple(x)
print y
