import random
d=int(input("Введите цифру в диапазоне 0-9: "))
lista= [random.randint(0,9) for x in range(15)]
print(lista)
#for x,y in enumerate(list)
if d in lista:
    for index, element in enumerate(lista):
        if element ==d:
            print("Ваша цифра:", element, ", под номером :", index, "в списке")
else:
    print("nicht")
