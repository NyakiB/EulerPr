def get_digit(number, n):
    return number//10**n%10

def collatz(k):
    store={}
    for i in range(1,k):
        n,steps=i,0
        while n!=1:
            if n%2==0:
                n=n//2
                steps+=1
            else:
                steps+=1
                n=n*3+1
        store[i]=steps
    return store

millioncollatz=collatz(1000000)
print(max(millioncollatz,key=millioncollatz.get))

