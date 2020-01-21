letters = "marvin, the paranoid android"
listletters = list(letters)

for i in listletters[:6]:
    print('\t'*2, i)

for i in listletters[-7:]:
    print('\t'*3, i)

for i in listletters[12:20]:
    print('\t'*4, i)

for i in listletters[-1::-1]:
    print(i, end="")
