year = int(input("Введите год: "))
if(year%4==0 and year%100!=0 or year%400==0):
    leap = True
    print("Високосный")
else:
    leap = False
    print("Не високосный")
op = int(input("Выберите сколько дней в:\n1.Январе\n2.Феврале\n3.Марте\n4.Апреле\n5.Мае\n6.Июне\n7.Июле\n8.Августе\n9.Сентябре\n10.Октябре\n11.Ноябре\n12.Декабре\n13.Году\n"))
sum=0
d=1
if (op==13):
    while d<13:
        if (d==2):
            if (leap==True):
                days=29
                for i in range(days+1):
                    while i>0:
                        des=i%10
                        sum+=des
                        i//=10
            else:
                days=28
                for i in range(days+1):
                    while i>0:
                        des=i%10
                        sum+=des
                        i//=10
            print(sum)
        elif (d%2!=0 or d==8):
            days=31
            for i in range(days+1):
                while i>0:
                    des=i%10
                    sum+=des
                    i//=10
            print(sum)
        else:
            days=30
            for i in range(days+1):
                while i>0:
                    des=i%10
                    sum+=des
                    i//=10
            print(sum)
        d+=1
elif (op%2!=0):
    days=31
    sum=0
    for i in range(days+1):
        print(i,":")
        while i>0:
            des=i%10
            sum+=des
            i//=10
            print(sum)
elif (op==2):
    if (leap == True):
        days=29
    else:
        days=28
    sum=0
    for i in range(days+1):
        print(i,":")
        while i>0:
            des=i%10
            sum+=des
            i//=10
            print(sum)
elif (op!=2 and op%2==0):
    days=30
    sum=0
    for i in range(days+1):
        print(i,":")
        while i>0:
            des=i%10
            sum+=des
            i//=10
            print(sum)
print(sum)