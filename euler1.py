numbers=list(range(0,1000))
x=len(numbers)
multiples=[]
divisor3=[]
divisor5=[]
for x in numbers:
    if x%3==0:
        divisor3.append(x)
        if x%5==0:
            multiples.append(x)
for x in numbers:
    if x%5==0:
        divisor3.append(x)

result=sum(divisor3)+sum(divisor5)-sum(multiples)
print(result)


            
