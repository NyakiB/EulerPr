numbers=list(range(1,101))
square=[]
summa=sum(numbers)
sumsqre=summa**2
for i in numbers:
    square.append(i**2)

result=sumsqre-sum(square)
print(result)
