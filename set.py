#creacion de un conjunto
numero = {1, 2, 3, 4, 5, 6}
print(type(numero))

#creacion de una tupla, no permite modificacion despues de creada
amor = ("ai", "love", "hate")
print(type(amor))

#creacion de conjuntos los cuales no permiten elementos repetidos
vowels = set('aeiou')
print("Provide a word to search for vowels: ")
word = input()

#funcion union para unir dos conjuntos
u = vowels.union(set(word))
print("funcion union: ", u)

#funcion intercepcion para ver elementos en comun
i = vowels.intersection(set(word))
print("funcion interseccion: ", i)

#funcion diferencia para ver lo que hay en un conjunto pero no en otro
d = vowels.difference(set(word))
print("funcion diferencia: ", d)
