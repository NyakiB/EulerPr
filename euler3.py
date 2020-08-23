number=600851475143
def primes(n):
    s=list(range(0,n+1))
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
            while (bottom<=top):
                    if s[top]:
                            s[top*bottom]=0
                    top-=1
            bottom+=1
            top=n//bottom
    return [x for x in s if x]
devidable=[]
prim=primes(1000000000)
for x in prim:
    if number%x==0:
        devidable.append(x)
print(max(devidable))
