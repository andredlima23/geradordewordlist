import itertools

string = input("Digite a string para ser permutada: ")

resultado = itertools.permutations(string, len(string))
for i in resultado:
    print(''.join(i))