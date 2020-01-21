#creacion de funciones en python la cual recibe un argumento
def search4vowels(word):
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for i in sorted(found):
        print(i, end = ' ')
    print()

#se le agrega valor por defecto si no es dado en el llamado de la funcion
def search4vowelsret(word : str, letters : set = {'a','e','i','o','u'}) -> bool:
    """documentacion de la funcion: se va a recibir un parametro de tipo cadena y retornara un valor booleano, 
    se mostrara con el comando help"""
    return bool(letters.intersection(set(word)))

#llamado de la funcion
print("input a phrase to search for vowels: ")
word = input()
search4vowels(word)

print(search4vowelsret(word))

#impresion de la documentacion de la funcion
print(help(search4vowelsret))
