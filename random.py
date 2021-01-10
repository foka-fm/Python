def abc(a,b,c):
    print("a= %s b= %s c= %s" %(a,b,c))
    while a+c<b:
        a=a+c
        print(a, "пока что нет")
    print("Дождались!", a+c)

abc(100,341,40)

