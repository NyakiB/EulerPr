years=[item for item in range(1901,2001)]
leap_years=[item for item in years if item%4==0]
months=[item for item in range(1,13)]
days=[]
for i in years:
    for j in months:
        if j in (1,3,5,7,8,10,12):
            for l in range(1,32):
                days.append(str(i)+'.'+str(j)+'.'+str(l))
        elif j in (3,6,9,11):
                for l in range(1,31):
                    days.append(str(i)+'.'+str(j)+'.'+str(l))
        else:
                if i in leap_years:
                    for l in range(1,30):
                        days.append(str(i)+'.'+str(j)+'.'+str(l))
                else:
                    for l in range(1,29):
                        days.append(str(i)+'.'+str(j)+'.'+str(l))

sundays=days[6::7]
count=sum([1 for item in sundays if int(item.split('.')[-1])==1])
print(count)
