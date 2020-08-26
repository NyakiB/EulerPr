from itertools import combinations
list1,list2=list(range(100,1000)),list(range(100,1000))
product,palindrome=[],[]
for x in list1:
    for y in list2:
        product.append(x*y)

for i in product:
    if str(i) == str(i)[::-1]:
        palindrome.append(i)

print(max(pelindrome))
    






    




