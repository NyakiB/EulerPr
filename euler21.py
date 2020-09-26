def divisor_gen(n):
    """The function returns the divisors of a number. It uses the quadratic sieve algorithm."""
    divisors=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            yield i
            if i is not n/i:
                divisors.insert(0,n//i)
    for div in divisors:
        if div!=n:
            yield div

def sum_div(n):
    storage={}
    for i in range(1,n+1):
        storage[i]=sum(divisor_gen(i))
    return storage

def ami_num(n):
    amicable_numbers = set()
    nmbrs=sum_div(n)
    for key, value in nmbrs.items():
        if value in nmbrs and nmbrs[value] == key and key != value:
            amicable_numbers.add(key)
            amicable_numbers.add(value)
    answer = sum(amicable_numbers)
    return answer
print(ami_num(10000))

        
