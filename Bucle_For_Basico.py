
#Numeros enteros del 1 al 150
from locale import LC_NUMERIC


for i in range(0, 151): #Agregamos una unidad mas al segundo elemento para que cuente el 150
    print(i)

#Multiplos de 5
for i in range(5,1001, 5):
    print(i)

#Contar como Dojo
for i in range(1,101):
    if (i % 5 == 0):
        print("Coding")
    elif (i % 10 == 0):
        print("Coging Dojo")
    else:
        print(i)

#Enteros impares
sum = 0 
for i in range(0, 500001,2):
    sum += i
print(sum)

#Cuenta regresiva de a 4
for i in range(2018,0,-4):
    print(i)

#Contador Flexible
lnum = 2
hnum = 9
mult = 3

for i in range(lnum,hnum + 1):
    if i % mult == 0:
        print(i)