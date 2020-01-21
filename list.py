#lista de diferentes tipos de objetos
car_details = ['Toyota', 'RAV4', 2.2, 60807]

#lista que contiene otra lista
everything = ['Hola', car_details]

odds_and_ends = [[1, 2, 3], ['a', 'b', 'c'], ['one', 'two', 'three']]

vowels = ['a', 'e', 'i', 'o', 'u']
#preguntar por una entrada de informacion por consola
word = input('introduce the word to search for vowels: ')

for i in vowels:
    if i in word:
        print(i)
print()

found = []
#calcula cual es el tamaño del objeto
len(found)

for i in word:
    if i in vowels and i not in found:
        print(i)
        #agrega un elemento a la lista
        found.append(i)       

num = [1, 2, 3, 4, 3, 5]
#elimina un elemento parecido de la lista que se encuentre de primero
num.remove(3)

#elimina un elemento de la posicion requerida, si no es dado elimina el ultimo
num.pop()

#inserta una lista y sus elementos a otra lista
num.extend([0, 4])

#inserta un elemento en la posicion deseada pero no en la ultima posicion
num.insert(2, "two an a half")
print(num)

phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)

compare = "on tap"
for i in plist:
    if i not in compare:
        plist.remove(i)

for i in range(3):
    plist.pop()

plist.insert(2, " ")
plist[4] = "a"

final = "".join(plist)
print(final)

#para asignar los valores de una lista a otra se usa copy y no =
plist2 = plist.copy()
plist2.append("h")

print(plist)
print(plist2)

#list slices
print(plist2[0: 10: 2])
