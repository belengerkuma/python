import pprint

print("introduce the word to find how many vowels have: ")
word = input()

#creacion de la estructura diccionario
found = {}
vowels = ['a', 'e', 'i', 'o', 'u']

for i in word:
    if i in vowels:
        #crea la llave por defecto y le asigna un valor si no esta creada en el diccionario
        found.setdefault(i, 0)
        found[i] += 1

#imprimir de manera organizada en pantalla
pprint.pprint(found)

#para que acceda al diccionario de manera ordenada
for i in sorted(found):
    print(i , "was found", found[i], "times")

#uso de variables para acceder al diccionario por items
for k, v in sorted(found.items()):
    print(k , "was found", v, "times")    
