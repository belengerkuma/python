from datetime import datetime
import time
import random
from datetime import date

#arreglo
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29,
        31, 33, 35, 37, 39, 41, 43, 45, 49, 51, 53, 55, 57, 59]

#variable asignada a los minutos del presente
right_this_minute = datetime.today().minute

#imprime el dia y la hora actual
print(datetime.today())

#imprime solo el dia actual
print(date.today())

#imprime la hora y los minutos
print(time.strftime("%H:%M"))

#imprime el dia en texto y si es de tarde o de mañana
print(time.strftime("%A %p"))

#uso del if
if right_this_minute in odds:
    print("This minute seems a little odd.")
else:
    print("Not a odd minute.")

if time.strftime("%A") == "Wednesday":
    print("A good day to learn")
elif time.strftime("%A") == "Monday":
    print("Awful day")
else:
    print("Not today")    

#uso del for en una cadena de texto
for i in "Homme":
    print(i)

#uso del for en una lista
for i in [1, 2, 3, "Homero"]:
    print(i)

#uso del for en un numero determinado de iteraciones
for i in range(1, 4, 1):
    print(i)

#dormir la ejecucion por 3 seg
time.sleep(3)

#numero al azar entre un rango y otro
print(random.randint(1, 60))
